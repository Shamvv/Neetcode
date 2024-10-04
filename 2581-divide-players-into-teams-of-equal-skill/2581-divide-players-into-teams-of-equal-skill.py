class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_skill = sum(skill)
        
        if total_skill % (n // 2) != 0:
            return -1
        
        target_skill_per_team = total_skill // (n // 2)
        skill.sort()
        total_chemistry = 0
        
        for i in range(n // 2):
            player1 = skill[i]
            player2 = skill[n - 1 - i]
            
            if player1 + player2 != target_skill_per_team:
                return -1
            
            total_chemistry += player1 * player2
        
        return total_chemistry