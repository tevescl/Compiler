z := 2;
if z < 3 then
  z := 1
else
  z := 0
end

# Running the parser/ply-parser by python3 parser.py < program2.py > tree will produce the file tree which contains

# Statements
#     Assign
#         z
#         2
#     If-Else
#         <
#             z
#             3
#         Statements
#             Assign
#                 z
#                 1
#         Statements
#             Assign
#                 z
#                 0
