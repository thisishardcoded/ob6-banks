import sys

sysex_file = sys.argv[1]
i = 0
pos = 4
old_bank = -1
new_bank = sys.argv[2]

with open(sysex_file, "rb") as f:
    patch_data = list(f.read())
    for byte in patch_data:
        if (i == pos):
            this_bank = byte
            if(not(old_bank > -1 and this_bank != old_bank)):
                old_bank = this_bank
            patch_data[pos] = int(new_bank)
            pos = pos + 1178
        i = i + 1
with open(sysex_file, "wb") as f:
    f.write(bytes(patch_data))

print(f"\nSuccess!\nFor '{sysex_file}': bank was {old_bank} is now {new_bank}.\n")
