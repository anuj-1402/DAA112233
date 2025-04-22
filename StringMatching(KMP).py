def compute_lps(pattern):
    """
    Builds the LPS (Longest Prefix Suffix) array.
    This array is used to avoid redundant comparisons in the main search.
    """
    lps = [0] * len(pattern)  # Initialize LPS array with 0s
    length = 0  # Length of the previous longest prefix suffix

    i = 1  # Start from second character
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # Characters match, increment length and assign to lps[i]
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Fall back to the last known good prefix
                length = lps[length - 1]
            else:
                # No prefix match, so set lps[i] to 0
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    Performs the KMP search on the text with the given pattern.
    Returns a list of starting indices where the pattern is found in the text.
    """
    lps = compute_lps(pattern)
    result = []

    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            # Pattern matched
            result.append(i - j)
            j = lps[j - 1]  # Look for next possible match

        elif i < len(text) and text[i] != pattern[j]:
            # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


# Test case
text = "ababcababcabc"
pattern = "ababc"

matches = kmp_search(text, pattern)
print("Pattern found at indices:", matches)
