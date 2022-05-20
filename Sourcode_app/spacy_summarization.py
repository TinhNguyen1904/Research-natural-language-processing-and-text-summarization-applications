#Cài đặt thư viện
import spacy
from spacy.lang.en.examples import sentences
nlp = spacy.load("en_core_web_sm")
nlp.Defaults.stop_words |={"cũng","của","cho","các","còn","có","khi","là","làm","ngoài","nhiều","như","nhất","những","này","nó","ra","sau","theo","thuộc","trong","trên","tại","từ","và","vào","về","với","xem","đã","đó","được","đến","để"}
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
#Thư viện tìm N câu hàng đầu
from heapq import nlargest



def text_summarizer(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Xây dựng tần suất từ
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    #Mã câu
    sentence_list = [ sentence for sentence in docx.sents ]

    #Điểm câu
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]


    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    return summary
    
