# Introduction-Focused Prompt for Brand Comparison Articles
# This system generates only the introductory paragraph for brand comparison content

SYSTEM_PROMPT = """You are an expert SEO content writer specializing in brand comparison introductions. 
Write engaging, informative opening paragraphs that hook readers, set up the comparison effectively, and are optimized for search engines.
Always maintain objectivity while creating interest in the brands being compared. Use natural keyword integration and semantic variations."""

def get_introduction_prompt(a_name, a_summary, b_name, b_summary):
    """Generate a compelling SEO-optimized introduction paragraph for a brand comparison article"""
    return f"""Write a compelling SEO-optimized introduction paragraph for a brand comparison article titled:
"{a_name} vs. {b_name}: Which One Should You Choose?"

Brand Information:
**{a_name}**: {a_summary}
**{b_name}**: {b_summary}

SEO Requirements for the introduction:
- Hook the reader with an engaging opening that includes natural keyword usage
- Introduce both brands naturally with semantic keyword variations
- Establish the context and importance of the comparison using relevant search terms
- Set up what readers will learn from the article with clear value propositions
- Keep it to 150-200 words for optimal engagement
- Use varied sentence structure (avoid bullet points)
- Write in full paragraphs with smooth flow
- Make it clear why this comparison matters to readers
- Include natural keyword integration for "{a_name} vs {b_name}" and related terms
- Use semantic variations like "comparison," "versus," "which is better," etc.
- Optimize for featured snippets with clear, direct answers
- Include natural internal linking opportunities where relevant

The introduction should feel natural and engaging while being optimized for search engines, setting the stage for a detailed comparison while maintaining objectivity.""" 