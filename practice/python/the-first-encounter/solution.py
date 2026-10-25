def string_to_number_mapping(s: str) -> dict:
    result = {}
    for i, ch in enumerate(s):
      if ch not in result:
        result[ch] = i    
    
    return result
