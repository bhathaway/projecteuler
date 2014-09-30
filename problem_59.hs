import Data.Bits
import Data.Char
import qualified Data.ByteString.Char8 as BC

split [] = []

split (c : []) = [[c]]

split (',' : input) = case (split input) of
    [] -> []
    x : r -> [] : (x:r)

split (c : input) = case (split input) of
    [] -> []
    x : r -> (c:x) : r

-- Need to define the decoder.

cyclicItem list index = list !! (index `mod` (length list))

longkey list n = map (cyclicItem list) [0..n-1]


decipher cipher key = decipher_helper cipher $ longkey key $ length cipher

decipher_helper [] [] = []

decipher_helper (cipher_head:cipher_rest) (key_head:key_rest) =
    cipher_head `xor` key_head : (decipher_helper cipher_rest key_rest)

containsWord word text =
    let text_bs = BC.pack text
        word_bs = BC.pack word in
            case (BC.findSubstring word_bs text_bs) of
                Just _ -> True
                Nothing -> False

main = do
    src <- readFile "cipher1.txt"
    let readInt x = read x :: Int
        cipher = map readInt (split src)
        case_list = [ord 'a' .. ord 'z']
        texts = [map chr $ decipher cipher [x, y, z] | x<-case_list, y<-case_list, z<-case_list] in
            print $ filter (containsWord "there") texts
    return ()
