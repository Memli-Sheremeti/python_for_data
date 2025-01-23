def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call to many times")
                return count
            count += 1
            function()
            return count
        return limit_function
    return callLimiter


def main():
    return


if __name__ == "__main__":
    main()
