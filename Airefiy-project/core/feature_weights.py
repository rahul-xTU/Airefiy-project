import re

class LinguisticFeatureAnalyzer:
    """
    Analyzes text to extract custom linguistic heuristic weights, 
    comparing empirical academic markers against sensationalized or exaggerated phrasing.
    """
    
    def __init__(self):
        # Dictionary of empirical, methodological, and rigorous academic markers
        self.empirical_lexicon = {
            "empirical", "observed", "measured", "evaluated", "statistically",
            "significant", "controlled", "quantified", "analyzed", "methodology",
            "framework", "baseline", "hypothesis", "validation", "cohort",
            "systematic", "robust", "variance", "correlation", "parameters"
        }
        
        # Dictionary of sensational, exaggerated, or predatory buzzwords
        self.sensational_lexicon = {
            "revolutionary", "miracle", "breakthrough", "unprecedented", "shocking",
            "mind-blowing", "ultimate", "guaranteed", "flawless", "magic",
            "secret", "definitively", "proven beyond doubt", "game-changer",
            "stunning", "radical", "overnight", "unstoppable"
        }

    def count_lexicon_matches(self, text: str, lexicon: set) -> int:
        """Counts the frequency of words from a specific lexicon present in the text."""
        if not text:
            return 0
        
        words = re.findall(r'\b[a-zA-Z\-]+\b', text.lower())
        match_count = sum(1 for word in words if word in lexicon)
        return match_count

    def compute_linguistic_scores(self, cleaned_text: str) -> dict:
        """
        Computes the raw counts and ratios of empirical vs sensational terms 
        to establish a heuristic risk profile.
        """
        if not cleaned_text:
            return {
                "empirical_score": 0.0,
                "sensational_score": 0.0,
                "linguistic_ratio_index": 0.0
            }

        word_list = cleaned_text.split()
        total_words = max(len(word_list), 1)  # Prevent division by zero

        empirical_hits = self.count_lexicon_matches(cleaned_text, self.empirical_lexicon)
        sensational_hits = self.count_lexicon_matches(cleaned_text, self.sensational_lexicon)

        # Normalize counts relative to text length (per 100 words)
        empirical_density = (empirical_hits / total_words) * 100
        sensational_density = (sensational_hits / total_words) * 100

        # Compute a balance index (higher means more empirical, lower/negative means more sensational)
        # Adding 1 to denominator to smooth values out
        ratio_index = (empirical_hits + 1) / (sensational_hits + 1)

        return {
            "empirical_matches": empirical_hits,
            "sensational_matches": sensational_hits,
            "empirical_density_per_100": round(empirical_density, 2),
            "sensational_density_per_100": round(sensational_density, 2),
            "linguistic_ratio_index": round(ratio_index, 2)
        }