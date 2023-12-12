def free_biscuits(games: dict[str, list[int]]) -> dict[str, bool]:
    """Determines which games UNC got free Bojangles biscuts."""
    result: dict[str, bool] = {}
    game_sum: int = 0
    for key in games: # loop through dict
        for player in games[key]: # loop through list in dict
            game_sum += player 
        # determine if result is true or false
        if game_sum > 99:
            result[key] = True
        else:
            result[key] = False
        # reset game_sum
        game_sum = 0
    return result


def max_key(given: dict[str, list[int]]) -> str:
    """Takes in a dict and outputs the key with the largest list."""
    # issue! if list has negative values, it will not 
    key: str = ""
    sum: int = 0 
    for pair in given:
        




def main():
    """Test cases."""
    # free_biscuits
    print(free_biscuits({ "UNCvsDuke": [38, 20, 42] , "UNCvsState": [9, 51, 16, 23] }))

    # max_key
    print(f'"b" == {max_key({"a": [1,2,3], "b": [4,5,6]})}')

if __name__ == "__main__":
    main()