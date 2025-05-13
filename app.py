import streamlit as st
from PyPDF2 import PdfReader
from ultils import text,   processo_embeedings
from streamlit_chat import message
  
def main ():
  st.set_page_config(page_title='Converse com chat', page_icon=':books:')  # Criando nossa tela para fazer interface da pagina #
   
  st.header('Converse com seus arquivos ')
  user_question=st.text_input('Digite sua pergunta')  # Criando um input para o usuario fazer a pergunta #
   
  if('conversation'not in st.session_state):  # Verificando se a conversaçao ja existe #
       st.session_state.conversation=None
   
  if (user_question):
      response=st.session_state. conversation (user_question)   # Pegando a resposta da conversaçao #
    
     
      for i, msg in enumerate(response):
          
          if(i%2==0):
           message(user_question, is_user=True, key=str(i)+ '_user')  # Pegando a pergunta do usuario #
          
          else:
           message(response["answer"], is_user=False, key=str(i)+ '_bot')   # Pegando a resposta da conversaçao #
    
   
  with st.sidebar:
       st.subheader('Seus arquivos')    
        
       pdf_docs=st.file_uploader("Carregue os seus arquivos pdf", accept_multiple_files=True)  # Metédo para carregar os arquivos pdf  , coloquei um paramentro para caregar mais de um arquivo #
       print(pdf_docs)
       if st.button('processar'):
         all_files_text=text.processos_files(pdf_docs)   #CHAMEI A FUNÇÃO QUE VAI PROCESSAR OS ARQUIVOS PDF E TRANSFORMAR EM TEXTO #
         
         chunks=text.create_text_chunks(all_files_text) 
         
         vectorstore=processo_embeedings.create_vectorstore(chunks)
         print(vectorstore)
        # print(all_files_texdt)  
       
         st.session_state.conversation = processo_embeedings.create_conversaçao_chain(vectorstore)
     
      
if __name__ == "__main__":
  main()  