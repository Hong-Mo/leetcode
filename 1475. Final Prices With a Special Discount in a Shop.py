class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        checkout = []
    
        for i in range(0, len(prices)):

            price = prices[i]

            for j in range(i+1, len(prices)):

                if prices[j] <= prices[i]:
                    price = prices[i] - prices[j]
                    break

            checkout.append(price)

        return checkout