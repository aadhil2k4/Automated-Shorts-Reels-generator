try:
    import google.generativeai as genai
    print("google.generativeai imported successfully!")
except ImportError as e:
    print(f"ImportError: {e}")
