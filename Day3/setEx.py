# A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
# Write a Python program that:
# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.
day1 = ["alice@example.com", "bob@example.com", "alice@example.com", "carol@example.com"]
day2 = ["bob@example.com", "alice@example.com", "eve@example.com"]
day3 = ["carol@example.com", "bob@example.com", "alice@example.com", "alice@example.com"]
def clean(elist):
    return set(email.lower() for email in elist)
c_day1 = clean(day1)
c_day2 = clean(day2)
c_day3 = clean(day3)
all_days = c_day1 | c_day2 | c_day3
attended_all_days = c_day1 & c_day2 & c_day3
one_day = (c_day1 - c_day2 - c_day3) | (c_day2 - c_day1 - c_day3) | (c_day3 - c_day1 - c_day2)
day12_overlap = c_day1 & c_day2
day23_overlap = c_day2 & c_day3
day31_overlap = c_day3 & c_day1
print("---Final Report---")

print(f"Total number of unique attendees: {len(all_days)}")
print(f"List of attendees who attended all three days: {sorted(attended_all_days)}")
print(f"Attendees who attended exactly one day: {sorted(one_day)}")


print("\nPairwise overlap counts:")
print(f"Day 1 & Day 2 overlap: {len(day12_overlap)} attendees")
print(f"Day 2 & Day 3 overlap: {len(day23_overlap)} attendees")
print(f"Day 1 & Day 3 overlap: {len(day31_overlap)} attendees")

print("\nPeople who attended both days:")
print(f"Day 1 & Day 2 overlap attendees: {sorted(day12_overlap)}")
print(f"Day 2 & Day 3 overlap attendees: {sorted(day23_overlap)}")
print(f"Day 1 & Day 3 overlap attendees: {sorted(day31_overlap)}")

