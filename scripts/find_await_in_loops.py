import os
import re

def find_await_in_loops(directory):
    await_pattern = re.compile(r'\bawait\b')
    loop_patterns = [
        re.compile(r'\bfor\s*\('),
        re.compile(r'\bfor\s+const\b'),
        re.compile(r'\bfor\s+let\b'),
        re.compile(r'\bwhile\s*\('),
        re.compile(r'\.forEach\s*\(\s*async'),
        re.compile(r'\.map\s*\(\s*async')
    ]

    results = []

    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        for file in files:
            if file.endswith('.js'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Very simple and naive detection of await in loops
                    # We look for a loop keyword and then an await before the closing brace
                    # This won't handle nested blocks perfectly but is a good start

                    lines = content.splitlines()
                    for i, line in enumerate(lines):
                        for lp in loop_patterns:
                            if lp.search(line):
                                # Found a loop start on line i
                                # Look for await in subsequent lines until we see what looks like a closing brace at same indentation
                                # (extremely simplified)
                                j = i
                                brace_count = line.count('{') - line.count('}')
                                while j < len(lines) - 1:
                                    j += 1
                                    sub_line = lines[j]
                                    if await_pattern.search(sub_line):
                                        results.append(f"{path}:{j+1} - Potential await in loop starting at line {i+1}")
                                        # break # Found one, move to next loop
                                    brace_count += sub_line.count('{') - sub_line.count('}')
                                    if brace_count <= 0:
                                        break
    return results

if __name__ == "__main__":
    for res in find_await_in_loops('js'):
        print(res)
