from enum import Enum


class ReportType(Enum):
    ResearchReport = "research_report"
    ResourceReport = "resource_report"
    OutlineReport = "outline_report"
    CustomReport = "custom_report"
    DetailedReport = "detailed_report"
    SubtopicReport = "subtopic_report"
    
    # MyTrip Exclusive
    SEOArticle = 'seo_article'
    ShipReview = 'ship_review'
    LuxuryCruiseDestination = 'luxury_cruise_destination'


class ReportSource(Enum):
    Web = "web"
    Local = "local"
    LangChainDocuments = "langchain_documents"
    Sources = "sources"
    Hybrid = "hybrid"


class Tone(Enum):
    Objective = "Objective (impartial and unbiased presentation of facts and findings)"
    Formal = "Formal (adheres to academic standards with sophisticated language and structure)"
    Analytical = (
        "Analytical (critical evaluation and detailed examination of data and theories)"
    )
    Persuasive = (
        "Persuasive (convincing the audience of a particular viewpoint or argument)"
    )
    Informative = (
        "Informative (providing clear and comprehensive information on a topic)"
    )
    Explanatory = "Explanatory (clarifying complex concepts and processes)"
    Descriptive = (
        "Descriptive (detailed depiction of phenomena, experiments, or case studies)"
    )
    Critical = "Critical (judging the validity and relevance of the research and its conclusions"
    Comparative = "Comparative (juxtaposing different theories, data, or methods to highlight differences and similarities)"
    Speculative = "Speculative (exploring hypotheses and potential implications or future research directions)"
    # Reflective = "Reflective (considering the research process and personal insights or experiences)"
    Narrative = (
        "Narrative (telling a story to illustrate research findings or methodologies)"
    )
    Humorous = "Humorous (light-hearted and engaging, usually to make the content more relatable)"
    Optimistic = "Optimistic (highlighting positive findings and potential benefits)"
    Pessimistic = (
        "Pessimistic (focusing on limitations, challenges, or negative outcomes)"
    )
    
    # MyTrip Exclusive
    Authoritative = "Authoritative (EEAT, Emphasizing First-hand Experience, Expertise, Authority, and Trustworthiness)"
    Inspirational = "Inspirational (Motivating and uplifting, encouraging readers to take action or pursue their goals)"
    Reflective = "Reflective (Thoughtful and introspective, encouraging readers to ponder and consider their own experiences or views)"
    Technical = "Technical (Detailed and precise, using industry-specific terminology for expert audiences)"
    Conversational = "Conversational (Friendly and relatable, engaging the reader in a dialogue as if speaking directly to them)"
    Urgent = "Urgent (Pressing and immediate, creating a sense of urgency to prompt quick action or decision-making)"
