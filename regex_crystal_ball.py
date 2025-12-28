#!/usr/bin/env python3
"""Regex Crystal Ball - Because regex debugging should involve less tears."""

import re
import sys

def regex_crystal_ball(pattern, test_strings):
    """
    Peek into the regex future. Spoiler: it's mostly disappointment.
    
    Args:
        pattern: Your regex masterpiece (or disaster)
        test_strings: List of strings to test against the pattern
    
    Returns:
        Dict with matches and explanations
    """
    results = {
        "pattern": pattern,
        "tests": [],
        "summary": {"total": len(test_strings), "matches": 0, "fails": 0}
    }
    
    try:
        # Compile the regex - this is where dreams either compile or die
        compiled = re.compile(pattern)
        print(f"\n🔮 Crystal Ball activated for: {pattern}")
        print("-" * 50)
        
        for i, test_str in enumerate(test_strings, 1):
            match = compiled.fullmatch(test_str)  # fullmatch for exact matches
            
            # The moment of truth
            if match:
                status = "✅ MATCH"
                results["summary"]["matches"] += 1
                groups = match.groups()
                # Show captured groups if they exist
                if groups:
                    groups_info = f" | Groups: {groups}"
                else:
                    groups_info = ""
            else:
                status = "❌ NO MATCH"
                results["summary"]["fails"] += 1
                groups_info = ""
            
            # Print results with dramatic flair
            print(f"Test {i}: {status}")
            print(f"   String: '{test_str}'{groups_info}")
            
            # Store for the final report
            results["tests"].append({
                "string": test_str,
                "matched": bool(match),
                "groups": match.groups() if match else None
            })
        
        # The grand finale
        print("-" * 50)
        matches = results["summary"]["matches"]
        fails = results["summary"]["fails"]
        print(f"\n📊 Final Score: {matches}/{matches+fails} tests passed")
        
        if fails == 0:
            print("🎉 Perfect! Your regex actually works! (This is rare)")
        else:
            print(f"💔 {fails} test(s) failed. Back to the regex drawing board!")
        
    except re.error as e:
        # When your regex is so broken it won't even compile
        print(f"\n💥 Regex Error: {e}")
        print("Your pattern is malformed. Even the crystal ball is confused.")
        results["error"] = str(e)
    
    return results


def main():
    """Main function - because every script needs one"""
    if len(sys.argv) < 3:
        print("Usage: python regex_crystal_ball.py 'regex_pattern' 'test1' 'test2' ...")
        print("Example: python regex_crystal_ball.py '^\\d{3}-\\d{2}-\\d{4}$' '123-45-6789' 'abc-def-ghij'")
        sys.exit(1)
    
    pattern = sys.argv[1]
    test_strings = sys.argv[2:]
    
    regex_crystal_ball(pattern, test_strings)


if __name__ == "__main__":
    main()
