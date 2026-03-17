import time
import os

# ---------------------------------------------------------
# Project: AI Study Buddy Global Pro
# Version: 2.0 (Competition Ready)
# Description: Intelligent text analysis and summarization 
# ---------------------------------------------------------

def advanced_summarizer(text):
    """
    يقوم بتحليل النص واستخراج أهم النقاط والكلمات المفتاحية
    """
    print("\n[AI] Analyzing text structure and extracting insights...")
    time.sleep(1.5) # محاكاة تفكير الذكاء الاصطناعي
    
    # 1. تنظيف الكلمات واستخراج الكلمات المفتاحية (Keywords)
    words = text.split()
    # نختار الكلمات التي تزيد عن 5 حروف وننظفها من الرموز
    keywords = [w.strip(".,!?;:").lower() for w in words if len(w) > 5][:5]
    
    # 2. توليد التلخيص (Summarization)
    # نقسم النص إلى جمل ونأخذ أول 3 جمل مفيدة
    sentences = text.split('.')
    summary_points = [s.strip() for s in sentences if len(s) > 1][:3]
    
    return {
        "summary": summary_points,
        "keywords": keywords,
        "timestamp": time.ctime(),
        "word_count": len(words)
    }

def display_report(data):
    """
    تنسيق المخرجات بشكل جمالي واحترافي للمستخدم
    """
    print("\n" + "⭐" * 40)
    print("        ✨ AI STUDY BUDDY REPORT ✨        ")
    print("⭐" * 40)
    print(f"📅 Generated on: {data['timestamp']}")
    print(f"📊 Words Processed: {data['word_count']}")
    
    print("\n🔑 TOP KEYWORDS (Concepts):")
    if data['keywords']:
        print("   " + " | ".join(data['keywords']))
    else:
        print("   No complex keywords found.")
    
    print("\n📝 EXECUTIVE SUMMARY:")
    for i, point in enumerate(data['summary'], 1):
        if point:
            print(f"   {i}. {point}.")
    
    print("\n" + "=" * 40)
    print("   Ready for your next learning session!   ")
    print("=" * 40)

def main():
    # واجهة البرنامج الرئيسية
    print("Welcome to AI Study Buddy Global v2.0")
    print("The future of smart learning starts here.\n")
    
    user_input = input("Paste your lesson content or article below:\n> ")
    
    if len(user_input) > 30:
        # البدء في تحليل البيانات
        analysis_results = advanced_summarizer(user_input)
        # عرض التقرير النهائي
        display_report(analysis_results)
    else:
        print("\n❌ Error: Input text is too short. Please provide more content for analysis.")

if __name__ == "__main__":
    main()
