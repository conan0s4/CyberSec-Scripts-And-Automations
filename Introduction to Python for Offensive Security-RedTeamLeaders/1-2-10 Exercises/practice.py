




byt3 = [1,2,32,41,50]
int3 = 67

convByt3 = bytes(int3)
print(convByt3)


def B3t3syntax():



    ss =  bytes([240, 159, 152, 138])
    bb = ss.decode() # decoding/encoding  on default uses utf8
    print(bb)

    s = "😊"
    b = s.encode()
    print(list(b))

    # wb = only bytes
    #w = str only
    # we can specify or decode or encode if let say is file is in another format to lets much readable text than raw bytes
#    with open("file.txt", "wb" , encoding="utf-8") as p: # open file in byte more or str mode
#        p.write(b"byte me")
        #p.write(b"byte me".decode()) #decode to get a string (w)
        #p.write("text str ".encode)     (wb)


B3t3syntax()


