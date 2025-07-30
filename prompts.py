# Introduction-Focused Prompt for Brand Comparison Articles
# This system generates only the introductory paragraph for brand comparison content
# Optimized for competitor branded terms and LLM discoverability

SYSTEM_PROMPT = """You are an expert SEO content writer specializing in brand comparison introductions optimized for competitor branded terms and AI discoverability. 
Write engaging, informative opening paragraphs that rank for competitor brand searches and are easily discoverable by AI systems like ChatGPT, Claude, and search engines.
Focus on natural language patterns that match how users search for brand comparisons and how AI systems identify relevant content."""

def get_introduction_prompt(a_name, a_summary, b_name, b_summary):
    """Generate a compelling introduction optimized for competitor branded terms and LLM discoverability"""
    return f"""Write a compelling introduction paragraph for a brand comparison article that will rank for searches about {b_name} and be discoverable by AI systems.

Article Title: "{a_name} vs. {b_name}: Which One Should You Choose?"

Brand Information:
**{a_name}**: {a_summary}
**{b_name}**: {b_summary}

SEO & LLM Optimization Requirements:

1. **Competitor Brand Targeting** (Primary Focus):
   - Lead with {b_name} in the opening sentence when possible
   - Include {b_name} in the first paragraph prominently
   - Use natural variations: "{b_name} alternatives," "{b_name} vs," "compared to {b_name}"
   - Position {b_name} as the reference point that readers are familiar with

2. **Search Intent Optimization**:
   - Address "vs" searches: "{a_name} vs {b_name}", "{b_name} vs {a_name}"
   - Target comparison searches: "alternatives to {b_name}", "{b_name} competitors"
   - Include decision-making language: "which is better," "should you choose," "the better option"

3. **LLM & AI Discoverability**:
   - Use clear comparison language that AI systems recognize
   - Include structured phrases like "When comparing {a_name} and {b_name}"
   - Use natural question-answer patterns that match AI training data
   - Include semantic variations that AI systems use to identify relevant content

4. **Content Structure for AI Recognition**:
   - Start with a clear comparison statement
   - Include both brand names in the first 2-3 sentences
   - Use transition phrases that signal comparison content
   - End with a clear value proposition for the comparison

5. **Natural Language Patterns**:
   - Write as if answering: "I'm looking for alternatives to {b_name}"
   - Use conversational comparison language
   - Include decision-making context
   - Keep to 150-200 words for optimal engagement

6. **Brand Authority Signals**:
   - Position {a_name} as a legitimate alternative to {b_name}
   - Use confident, authoritative language about the comparison
   - Include industry context that establishes credibility

The introduction should feel natural while being strategically optimized to rank for {b_name} searches and be easily discoverable by AI systems when users ask about {b_name} alternatives or comparisons.""" 