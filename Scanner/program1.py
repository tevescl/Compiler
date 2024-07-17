z := 2;
if z < 3 then
  z := 1
end

# Running the scanner/ply-scanner by python3 scanner.py < program1.py > tokens will produce the file tokens which contains

# ID z
# BEC
# NUM 2
# SEM
# IF
# ID z
# LESS
# NUM 3
# THEN
# ID z
# BEC
# NUM 1
# END
