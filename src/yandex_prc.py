import sys


def main():
    def min_path_cost():
        N, M = map(int, input().split())
        cost = [list(map(int, input().split())) for _ in range(N)]
        dp = [[0] * M for _ in range(N)]
        dp[0][0] = cost[0][0]
        for i in range(1, M):
            dp[0][i] = dp[0][i - 1] + cost[0][i]
        for i in range(1, N):
            dp[i][0] = dp[i - 1][0] + cost[i][0]
        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]
        return dp[-1][-1]

    print(min_path_cost())
    pass


if __name__ == '__main__':
    main()