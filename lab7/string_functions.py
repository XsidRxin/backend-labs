import re

def format_product_info(name, quantity, base_price):
    total_price = quantity * base_price
    discount = calculate_discount(total_price)
    
    template = "Product: {}, Quantity: {}, Unit Price: ${:.2f}, Total: ${:.2f}, Discount: ${:.2f}, Final Price: ${:.2f}"
    final_price = total_price - discount
    
    return template.format(name, quantity, base_price, total_price, discount, final_price)


def calculate_discount(price):
    if price > 100:
        return price * 0.1
    elif price > 50:
        return price * 0.05
    return 0


def print_pattern(pattern, separator, repetitions):
    result = []
    for i in range(1, repetitions + 1):
        result.append(separator.join([pattern] * i))
    
    output = "\n".join(result)
    print("Pattern output:")
    print(output)
    return output


def count_substring_insensitive(text, substring):
    if not substring:
        return 0
    
    text_lower = text.lower()
    substring_lower = substring.lower()
    count = 0
    start = 0
    
    while True:
        pos = text_lower.find(substring_lower, start)
        if pos == -1:
            break
        count += 1
        start = pos + len(substring_lower)
    
    return count


def extract_substring(text, start_idx, end_idx):
    """Step 4: Extract substring between indices. One-liner implementation."""
    return text[start_idx+1:end_idx] if 0 < start_idx < len(text)-1 and 0 < end_idx <= len(text) else ""


def find_latin_in_cyrillic(*texts):
    visual_lookalikes = set('AEHKMOPCTXYBaehkmopxy')
    affected_strings = []
    total_affected_words = 0
    
    for text in texts:
        words = text.split()
        string_affected_count = 0
        
        for word in words:
            has_latin = any(c in visual_lookalikes for c in word)
            if has_latin:
                string_affected_count += 1
        
        if string_affected_count > 0:
            affected_strings.append(text)
            total_affected_words += string_affected_count
    
    return affected_strings, total_affected_words


def is_palindrome(text):
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]


def clean_whitespace(text):
    cleaned = ' '.join(text.split())
    return len(cleaned)


def replace_sentence_endings(text):
    result = re.sub(r'[.!?]+', '\n', text)
    return result.strip()


def reverse_words(text):
    words = text.split()
    return ' '.join(reversed(words))


def capitalize_after_punctuation(text):
    result = []
    capitalize_next = False
    
    for i, char in enumerate(text):
        if char in '.!?':
            result.append(char)
            capitalize_next = True
        elif capitalize_next and char != ' ':
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
    
    return ''.join(result)


def extract_camelcase_words(text):
    pattern = r'\b[a-z]+[A-Z][a-zA-Z]*\b'
    return re.findall(pattern, text)


def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def remove_duplicate_chars(text):
    result = []
    prev_char = None
    
    for char in text:
        if char != prev_char:
            result.append(char)
            prev_char = char
    
    return ''.join(result)


def run_all_demonstrations():
    
    print("=" * 70)
    print("STRING PROCESSING DEMONSTRATION")
    print("=" * 70)
    
    print("\n--- String Interpolation ---")
    result1 = format_product_info("Laptop", 5, 29.99)
    print(result1)
    
    print("\n--- Pattern Repetition ---")
    print_pattern("*", "-", 4)
    
    print("\n--- Substring Count (Case-Insensitive) ---")
    text3 = "The Quick brown fox jumps over the lazy dog. The fox is quick."
    substring3 = "the"
    count3 = count_substring_insensitive(text3, substring3)
    print(f'Text: "{text3}"')
    print(f'Substring: "{substring3}"')
    print(f'Count: {count3}')
    
    print("\n--- Extract Substring By Indices ---")
    text4 = "Programming in Python"
    start_idx = 2
    end_idx = 13
    extracted = extract_substring(text4, start_idx, end_idx)
    print(f'Text: "{text4}"')
    print(f'Indices [{start_idx}:{end_idx}]: "{extracted}"')

    print("\n--- Latin Letters in Cyrillic Text ---")
    text5a = "Привет мир и программирование на Python"
    text5b = "Это текст с латинскими буквами как O и A"
    text5c = "Все кириллица в этом тексте"
    
    affected, count = find_latin_in_cyrillic(text5a, text5b, text5c)
    print(f"Text 1: {text5a}")
    print(f"Text 2: {text5b}")
    print(f"Text 3: {text5c}")
    print(f"Affected strings: {affected}")
    print(f"Total affected words: {count}")
    
    print("\n--- Palindrome Check ---")
    test_strings = ["race car", "12321", "hello", "A man a plan a canal Panama"]
    for s in test_strings:
        is_pal = is_palindrome(s)
        print(f'"{s}" -> {is_pal}')
    
    print("\n--- Whitespace Cleanup ---")
    text7 = "   This   is   a    text   with   extra    spaces   "
    length7 = clean_whitespace(text7)
    cleaned = ' '.join(text7.split())
    print(f'Original: "{text7}"')
    print(f'Cleaned: "{cleaned}"')
    print(f'Length: {length7}')
    
    print("\n--- Replace Sentence Endings ---")
    text8 = "Hello world! This is test. Are you ready? Yes!"
    result8 = replace_sentence_endings(text8)
    print(f'Original: "{text8}"')
    print(f'Result:\n{result8}')
    
    print("\n--- Additional String Algorithms ---")
    
    text9a = "The quick brown fox jumps"
    reversed_words = reverse_words(text9a)
    print(f"\n9.1 Reverse words:")
    print(f'Original: "{text9a}"')
    print(f'Reversed: "{reversed_words}"')
    
    text9b = "hello. world! are you ok? yes."
    capitalized = capitalize_after_punctuation(text9b)
    print(f"\n9.2 Capitalize after punctuation:")
    print(f'Original: "{text9b}"')
    print(f'Result: "{capitalized}"')
    
    text9c = "This is myVariable and anotherOne complex implementation"
    camelcase = extract_camelcase_words(text9c)
    print(f"\n9.3 Extract camelCase words:")
    print(f'Text: "{text9c}"')
    print(f'CamelCase words: {camelcase}')
    
    text9d = "the quick brown fox jumps over the lazy dog the fox is quick"
    frequency = word_frequency(text9d)
    print(f"\n9.4 Word frequency:")
    print(f'Text: "{text9d}"')
    print(f'Frequency: {frequency}')
    
    text9e = "aabbccddee hello mississippi"
    no_dupes = remove_duplicate_chars(text9e)
    print(f"\n9.5 Remove duplicate consecutive characters:")
    print(f'Original: "{text9e}"')
    print(f'Result: "{no_dupes}"')
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETED")
    print("=" * 70)
