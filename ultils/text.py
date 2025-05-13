from PyPDF2 import PdfReader
from langchain.text_splitter import  CharacterTextSplitter  

def processos_files(files):
    text= ''
    
    for file in files:
        pdf=PdfReader(file)
        
        for page in pdf.pages:     # Vou iterar as paginas do arquivo pdf  para pegar todas paginas do pdf#
         
         text +=page.extract_text()    #   METEDO VAI EXTRAIR  OS TEXTOS E TRANSFORMAR EM STRING#
          
    return text
      
def create_text_chunks(text):        # CRIEI UMA  FUNÇAO QUE VAI SER RESPONSAVEL POR DIVIDIR MINHA STRING EM PARTES PEQUENAS #
    
    text_splitter=CharacterTextSplitter( separator='\n', chunk_size=1000, chunk_overlap=200, length_function=len )   # CRIEI UM OBJETO QUE VAI SER RESPONSAVEL POR DIVIDIR O TEXTO EM PARTES MENOR #)
    
    chunks= text_splitter.split_text(text)                                                                                                               # overlap e uma sobreposiçao do chunk anterior para frase nao ficar cortada #
    return chunks