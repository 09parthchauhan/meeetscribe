import os
import sys
import time
import requests
from dotenv import load_dotenv

load_dotenv()

def upload_and_transcribe(audio_file_path):
    """Upload audio to Sarvam Batch API and get transcription with diarization"""
    
    # Check file exists
    if not os.path.exists(audio_file_path):
        print(f"File not found: {audio_file_path}")
        return None
    
    # Get API key
    api_key = os.getenv('SARVAM_API_KEY')
    if not api_key:
        print("SARVAM_API_KEY not found in .env file")
        print("Get your key from: https://dashboard.sarvam.ai")
        return None
    
    print("Starting Sarvam AI Batch Transcription (HTTP API)\n")
    print(f"Audio file: {audio_file_path}")
    print(f"API key: {api_key[:10]}...{api_key[-4:]}\n")
    
    # API endpoint
    base_url = "https://api.sarvam.ai"
    
    try:
        # Step 1: Upload file and create batch job
        print("Uploading file to Sarvam Batch API...")
        
        upload_url = "https://api.sarvam.ai/speech-to-text"
        
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        
        # Open file
        with open(audio_file_path, 'rb') as f:
            files = {
                'file': (os.path.basename(audio_file_path), f, 'audio/mpeg')
            }
            
            data = {
                'model': 'saaras:v3',
                'mode':'transcribe',
                #'with_diarization': 'true',
                #'num_speakers': '2',
                #'with_timestamps': 'true'
            }
            

            response = requests.post(upload_url, headers=headers, files=files, data=data)
        
        if response.status_code != 200:
            print(f"Upload failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
        
        result = response.json()
        print(result) 
        return result
        
        # Step 2: Poll for completion
        status_url = f"{base_url}/v1/speech-to-text-translate/batch/{job_id}"
        
        max_wait = 600  # 10 minutes
        poll_interval = 10
        elapsed = 0
        
        while elapsed < max_wait:
            time.sleep(poll_interval)
            elapsed += poll_interval
            status_response = requests.get(status_url, headers=headers)
            
            if status_response.status_code != 200:
                print(f"Error checking status: {status_response.status_code}")
                continue
            
            result = status_response.json()
            status = result.get('status', 'UNKNOWN')
            
            print(f"{elapsed}s elapsed | Status: {status}")
            
            if status == 'COMPLETED':
                print("\nTranscription completed!\n")
                print("=" * 80)
                print("TRANSCRIPT:")
                print("=" * 80)
                
                transcript = result.get('transcript', '')
                print(transcript)
                
                # Check for diarized transcriptr
                if 'diarized_transcript' in result:
                    print("\n" + "=" * 80)
                    print("DIARIZED TRANSCRIPT (Speaker-wise):")
                    print("=" * 80)
                    
                    for segment in result['diarized_transcript']:
                        speaker = segment.get('speaker', 'Unknown')
                        text = segment.get('text', '')
                        start = segment.get('start_time', 0)
                        print(f"\n[{start:.1f}s] {speaker}: {text}")
                
                return result
                
            elif status == 'FAILED':
                print(f"\nJob failed: {result.get('error', 'Unknown error')}")
                return None
        
        print(f"\nTimeout after {max_wait}s. Job may still be processing.")
        return None
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


def generate_summary(transcript_text):
    """Use Sarvam-M to generate meeting summary"""
    
    api_key = os.getenv('SARVAM_API_KEY')
    if not api_key or not transcript_text:
        return None
    
    print("\n" + "=" * 80)
    print("Generating AI Summary with Sarvam-M")
    print("=" * 80)
    
    # Truncate if too long
    if len(transcript_text) > 4000:
        transcript_text = transcript_text[:4000] + "..."
    
    url = "https://api.sarvam.ai/v1/chat/completions"
    
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "sarvam-m",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful meeting assistant."
            },
            {
                "role": "user",
                "content": f"""Analyze this meeting transcript and provide:

1. Brief summary (2-3 sentences)
2. Key decisions made
3. Action items (with owners if mentioned)
4. Follow-up topics

Meeting Transcript:
{transcript_text}

Respond in JSON format with keys: summary, decisions, action_items, follow_ups"""
            }
        ],
        "temperature": 0.3,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code != 200:
            print(f"Summary failed: {response.status_code}")
            print(response.text)
            return None
        
        result = response.json()
        summary = result['choices'][0]['message']['content']
        
        print("\nAI-Generated Summary:\n")
        print(summary)
        
        return summary
        
    except Exception as e:
        print(f"Summary error: {str(e)}")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python poc_http_api.py <path-to-audio-file>")
        print("\nExamples:")
        print("  python poc_http_api.py meeting.mp3")
        print("  python poc_http_api.py ~/Downloads/call.wav")
        print("\nSupported: MP3, WAV, M4A, AAC, FLAC, OGG")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    print("=" * 80)
    print(" MEETSCRIBE POC - SARVAM AI HTTP API")
    print("=" * 80)
    
    # Test transcription
    result = upload_and_transcribe(audio_file)
    
    if result and result.get('transcript'):
        # Test summarization
        generate_summary(result['transcript'])
        
        print("\n" + "=" * 80)
        print("✅ POC TEST COMPLETE!")
        print("=" * 80)
        print("\n🎉 Sarvam API is working!")
    else:
        print("\n" + "=" * 80)
        print("❌ TEST FAILED")
        print("=" * 80)
        print("\nCheck:")
        print("1. SARVAM_API_KEY in .env")
        print("2. Audio file path is correct")
        print("3. File is valid audio (<1 hour)")