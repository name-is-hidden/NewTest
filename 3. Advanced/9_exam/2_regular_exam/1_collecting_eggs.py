eggs = [int(x) for x in input().split(", ")]
papers = [int(x) for x in input().split(", ")]

filled_boxes = 0

while True:
    if len(eggs) == 0 or len(papers) == 0:
        break

    current_egg = eggs[0]
    current_piece_of_paper = papers[-1]

    if current_egg <= 0:
        eggs.remove(current_egg)

    elif current_egg == 13:
        eggs.remove(current_egg)
        papers[0], papers[-1] = papers[-1], papers[0]

    elif (current_egg + current_piece_of_paper) <= 50:
        filled_boxes += 1
        eggs.remove(current_egg)
        papers.remove(current_piece_of_paper)

    else:
        eggs.remove(current_egg)
        papers.remove(current_piece_of_paper)

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")

else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")

if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")

########################################################################################################################

# from collections import deque
#
# egg_size = deque([int(x) for x in input().split(', ')])
# paper_size = deque([int(x) for x in input().split(', ')])
#
# box = 0
#
# while egg_size and paper_size:
#     egg = egg_size.popleft()
#     paper = paper_size.pop()
#
#     if egg == 13:
#         paper_size.append(paper)
#         paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
#
#     elif egg <= 0:
#         paper_size.append(paper)
#
#     elif egg + paper <= 50:
#         box += 1
#
# if box >= 1:
#     print(f'Great! You filled {box} boxes.')
# else:
#     print('Sorry! You couldn't fill any boxes!')
#
# if egg_size:
#     print(f'Eggs left: {", ".join([str(x) for x in egg_size])}')
# if paper_size:
#     print(f'Pieces of paper left: {", ".join([str(x) for x in paper_size])}')
