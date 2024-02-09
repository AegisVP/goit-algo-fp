

def greedy(dict, budget):
    sorted_items = sorted(dict.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    result = []
    current_cost = 0

    for name, params in sorted_items:
        if current_cost + params['cost'] <= budget:
            result.append({name: params})
            current_cost += params['cost']
    return result


def dynamic(dict, budget):
    def maxWeight(cost, num_items, prices, weights, memo=[[]]):
        if num_items <= 0 or cost <= 0:
            return 0
        if memo[num_items][cost] is not None:
            return memo[num_items][cost]

        if prices[num_items - 1] <= budget:
            mw1 = maxWeight(cost, num_items - 1, prices, weights, memo)
            mw2 = maxWeight(cost - prices[num_items - 1], num_items - 1, prices, weights, memo) + weights[num_items - 1]
            memo[num_items][cost] = max(mw1, mw2)
            return memo[num_items][cost]
        else:
            mw = maxWeight(cost, num_items - 1, prices, weights, memo)
            memo[num_items][cost] = mw
            return memo[num_items][cost]

    prices = []
    weight = []
    names = []
    for name, params in dict.items():
        cost, calories = params.values()
        prices.append(cost)
        weight.append(round(calories / cost, 5))
        names.append(name)

    memo = [[None for _ in range(budget + 1)] for _ in range(len(prices) + 1)]

    mxw = maxWeight(budget, len(prices), prices, weight, memo)
    ret_list = []

    for i in range(len(prices), 0, -1):
        if budget <= 0 or mxw <= 0:
            break

        if memo[i][budget] == mxw and prices[i - 1] <= budget:
            ret_list.append({names[i - 1]: dict[names[i - 1]]})
            budget -= prices[i - 1]
            mxw -= weight[i - 1]

    return ret_list


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 52

    print(f"Greedy algorythm: {greedy(items, budget)}")
    print(f"Dynamic algorythm: {dynamic(items, budget)}")
