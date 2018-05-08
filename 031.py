count = 0
l = []
for twoL in range(2):
    for oneL in range(3):
        if 200 * twoL + 100 * oneL > 200:
            break
        for fiftyP in range(5):
            if 200 * twoL + 100 * oneL + 50 * fiftyP > 200:
                break
            for twentyP in range(11):
                if 200 * twoL + 100 * oneL + 50 * fiftyP + 20 * twentyP > 200:
                    break
                for tenP in range(21):
                    if 200 * twoL + 100 * oneL + 50 * fiftyP + 20 * twentyP +\
                       10 * tenP > 200:
                        break
                    for fiveP in range(41):
                        if 200 * twoL + 100 * oneL + 50 * fiftyP + 20 * twentyP\
                           + 10 * tenP + 5 * fiveP > 200:
                            break
                        for twoP in range(101):
                            if 200 * twoL + 100 * oneL + 50 * fiftyP + 20 *\
                               twentyP + 10 * tenP + 5 * fiveP + 2 * twoP > 200:
                                break
                            l.append([twoL, oneL, fiftyP, twentyP, tenP, fiveP,\
                                      twoP, 200 - (200 * twoL + 100 * oneL + 50\
                                                   * fiftyP + 20 * twentyP + 10\
                                                   * tenP + 5 * fiveP + 2 *\
                                                   twoP)])
                            count += 1
print(count)
