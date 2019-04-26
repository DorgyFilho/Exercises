while True:
    try:
        seq = input().lower()
        nseq = seq.split('-')
        if (nseq[0][0] == 'c' or nseq[0][-1] == 'c') and (nseq[1][0] == 'o' or nseq[1][-1] == 'o') and (nseq[2][0] == 'b' or nseq[2][-1] == 'b') and (nseq[3][0] == 'o' or nseq[3][-1] == 'o') and (nseq[4][0] == 'l' or nseq[4][-1] == 'l'):
            print('GRACE HOPPER')
        else:
            print('BUG')
    except:
        break