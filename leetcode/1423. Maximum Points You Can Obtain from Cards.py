class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = 0
        untaken = len(cardPoints)-k
        score = 0
        total_score = sum(cardPoints)
        while r<untaken:
            score += cardPoints[r]
            r += 1
            
        min_score = score
        while r<len(cardPoints):
            score -= cardPoints[l]
            score += cardPoints[r]
            if min_score > score:
                min_score = score
            l += 1
            r += 1
                
        return total_score-min_score