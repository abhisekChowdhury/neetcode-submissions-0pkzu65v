class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # add self as follower
        self.followMap[userId].add(userId)

        for folowee in self.followMap[userId]:
            if folowee in self.tweetMap:
                for time, tweetId in self.tweetMap[folowee][-10:]:
                    heapq.heappush(heap, (-time, tweetId))
        
        res = []

        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
