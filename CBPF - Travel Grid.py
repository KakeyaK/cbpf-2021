import unittest
    
# Função de grid travel sem memorização
# viagens = 0
# def travel1(a, b, n, m):

#     global viagens

#     if(a == n and  b == m):
#         viagens += 1
#     if(a<n):
#         travel1(a+1, b, n, m)
#     if(b<m):
#         travel1(a, b+1, n, m)
    
# n,m = [int(x) for x in input("escolha m e n: ").split(" ")]
# print(travel2(m, n))

#=== Solução com memorização ===#

def travel2(m, n, dict = {}):

    if m == 1 or n == 1:
        return 1
    
    elif (m,n) in dict:
        return dict[(m,n)]
    
    elif (n, m) in dict:
        return dict[(n, m)]

    elif m > 0 and n > 0:
        dict[(m,n)] = travel2(m-1, n) + travel2(m, n-1)
        return travel2(m-1, n) + travel2(m, n-1)

class TestFib(unittest.TestCase):
    def test_values(self):
        expected = { (1, 1): 1,
                     (2, 3): 3,
                     (3, 2): 3,
                     (18, 18): 2333606220
                   }
        for key, exp_val in expected.items():
          got = travel2(key[0], key[1])
          self.assertEqual(exp_val, got)
    
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)