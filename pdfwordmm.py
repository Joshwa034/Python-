def designerPdfViewer(h, word):
    # Write your code here
    mx = 0

    for i in range (len(word)):
        if mx<h[ord(word[i])-97]:
            mx=h[ord(word[i])-97]

    res = mx*len(word)
    return (res)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)