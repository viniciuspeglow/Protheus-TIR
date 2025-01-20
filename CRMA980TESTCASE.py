from tir import Webapp
from datetime import datetime
import unittest
import time

DataSystem = datetime.today().strftime('%d/%m/%Y')


class CRMA980(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		
		inst.oHelper.Setup('SIGAFAT',DataSystem,'99','01','05')
		inst.oHelper.SetLateralMenu("Atualizações > Cadastros > Clientes")
		#inst.oHelper.Program('CRMA980')

# ------------------------------------------------------------------------------
# | FUNÇÃO - Incluir / Visualizar                                              |
# ------------------------------------------------------------------------------	
	def test_CRMA980_001(self):

		rodar_paramentros = 'N' # MV_ dentro do configurador (SIGACFG)
		tem_filial = 'N'
		
		filial = '01'
		cliente = 'BMTEC1'
		loja = '01'
		
		if rodar_paramentros == 'S':
			self.oHelper.AddParameter("MV_MVCSA1","",".T.",".T.",".T.")
			self.oHelper.AddParameter("MV_APICCGC","",".T.",".T.",".T.")  
			self.oHelper.SetParameters()
		else:
			pass

		self.oHelper.SetButton('Incluir')

		if tem_filial == 'S':
			self.oHelper.SetBranch(filial)
		else:
			pass
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.SetValue('A1_COD',cliente)
		self.oHelper.SetValue('A1_LOJA',loja)
		self.oHelper.SetValue('A1_CGC','27382110000111')
		self.oHelper.SetValue('A1_PESSOA','J - Juridica')
		self.oHelper.SetValue('A1_NOME','BM TEC BRASIL - INCLUSAO')
		self.oHelper.SetValue('A1_NREDUZ','BM TEC')
		self.oHelper.SetValue('A1_END','RUA CORACAO DE MARIA, 246')
		self.oHelper.SetValue('A1_TIPO','F - Cons.Final')
		self.oHelper.SetValue('A1_EST','RS')
		self.oHelper.SetValue('A1_COD_MUN','07708')
		self.oHelper.SetValue('A1_DDD','51')
		self.oHelper.SetValue('A1_TEL','31372070')

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse(f'{cliente+loja}', 'Codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)
		self.oHelper.CheckResult('A1_CGC','27382110000111')
		self.oHelper.CheckResult('A1_PESSOA','J - Juridica')
		self.oHelper.CheckResult('A1_NOME','BM TEC BRASIL - INCLUSAO')
		self.oHelper.CheckResult('A1_NREDUZ','BM TEC')
		self.oHelper.CheckResult('A1_END','RUA CORACAO DE MARIA, 246')
		self.oHelper.CheckResult('A1_TIPO','F - Cons.Final')
		self.oHelper.CheckResult('A1_EST','RS')
		self.oHelper.CheckResult('A1_COD_MUN','07708')
		self.oHelper.CheckResult('A1_DDD','51')
		self.oHelper.CheckResult('A1_TEL','31372070')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

# ------------------------------------------------------------------------------
# | FUNÇÃO - Alterar / Visualizar                                              |
# ------------------------------------------------------------------------------
	def test_CRMA980_002(self):

		cliente = 'BMTEC1'
		loja = '01'

		self.oHelper.SearchBrowse(f'{cliente+loja}', 'Codigo + Loja')

		self.oHelper.SetButton('Alterar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.SetValue('A1_TEL','982489999')
		self.oHelper.SetValue('A1_NOME','BM TEC BRASIL - ALTERACAO')
				
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')


		self.oHelper.SearchBrowse(f'{cliente+loja}', 'Codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)
		self.oHelper.CheckResult('A1_TEL','982489999')
		self.oHelper.CheckResult('A1_NOME','BM TEC BRASIL - ALTERACAO')
			
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()	

# ------------------------------------------------------------------------------
# | FUNÇÃO - Excluir                                                           |
# ------------------------------------------------------------------------------	
	def test_CRMA980_003(self):

		cliente = 'BMTEC1'
		loja = '01'

		self.oHelper.SearchBrowse(f'{cliente+loja}', 'Codigo + Loja')
		
		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)

		if self.oHelper.GetValue("A1_COD") == cliente and self.oHelper.GetValue("A1_LOJA") == loja:
			self.oHelper.SetButton('Confirmar')
			
			self.oHelper.WaitHide("Tem certeza que deseja excluir o item abaixo?")
			self.oHelper.SetButton('Fechar')
		else:
			self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()	
	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()