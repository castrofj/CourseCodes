class CryptoScript:

    def __init__(self,message, key):
        #input variables
        self.message = message
        self.key = key
        self.logic_selector = None
        
        #Auxiliary vectors
        self.m_list = []
        self.c_list = []
        self.m_result = []
        
        #Auxiliary variables
        self.tam = len(self.message)
        self.key_sum = 0

        #Output variables
        self.output = ""
        
        # popular variáveis m_list e c_list com vetores de caracteres
        count = 0
        for index in range(self.tam):
            self.m_list.append(self.message[index])
            self.c_list.append(self.key[count])
            count += 1
            if count == len(self.key):
                count = 0

        print(f"\nMensagem em formato lista:\n {self.m_list}")
        print(f"\nChave em formato lista:\n {self.c_list}")

        # converter caracteres de ambos vetores auxiliares m_list e c_list em ascii hex
        for index in range(self.tam):
            self.m_list[index] = ord(self.m_list[index])
            self.c_list[index] = ord(self.c_list[index])
            self.key_sum += self.c_list[index]

        print(f"\nMensagem em formato lista - hex: \n {self.m_list}")
        print(f"\nChave em formato lista - hex: \n {self.c_list}")
        #print(f"\n A somatória total da chave é: {self.key_sum}")

        # converter hex de ambos vetores auxiliares m_list e c_list em binario. 
        # Inclui lógica para complementar com 0 para elementos menores que 8 bits.
        for index in range(self.tam):
            self.m_list[index] = format(self.m_list[index], 'b')
            temp_i_m = self.m_list[index][::-1]
            while len(temp_i_m) < 8: # estudar maneira de alterar para uma variável que permita aplicações maiores a apenas ASCII
                temp_i_m += '0'
            self.m_list[index] = temp_i_m[::-1]
            
            self.c_list[index] = format(self.c_list[index], 'b')
            temp_i_c = self.c_list[index][::-1]
            while len(temp_i_c) < 8: # estudar maneira de alterar para uma variável que permita aplicações maiores a apenas ASCII
                temp_i_c += '0'
            self.c_list[index] = temp_i_c[::-1]

        print(f"\nMensagem em formato lista - bin: \n {self.m_list}")
        print(f"\nChave em formato lista - bin: \n {self.c_list}")

    #Funções lógicas
    def XOR(self, bitA, bitB):
        result = []    
        for index in range(len(bitA)):
            if int(bitA[index]) == int(bitB[index]):
                result.append('0')
            else:
                result.append('1')
        
        print(f"Resultado da operação XOR: \n{result}")
        
        result = ''.join(result)   
        
        return result
    
    def NAND(self, bitA, bitB):
        pass

    def AND(self, bitA, bitB):
        pass

    def OR(self, bitA, bitB):
        pass

    #função para arranjar cada elemento dos vetor m_list e c_list em 8 bits individuais. 
    # Em seguida aplica-se a lógica escolhida (XOR, AND, NAND, OR, etc.)
    def bit_work(self):
        m_bin = []
        c_bin = []
        XOR_result = ""
        print("\n=================== INÍCIO DA OPERAÇÃO XOR ========================")
        for i in range(self.tam):
            for j in range(8):
                m_bin.append(self.m_list[i][j])
                c_bin.append(self.c_list[i][j])
            
            print(f"\nVetor índice: {i+1}")
            print(f"{m_bin}")
            print(f"{c_bin}\n")   

            #alterar código aqui caso seja oferecido opção distinta a XOR. Incluir um if com variável seletora da lógica.
            XOR_result = self.XOR(m_bin, c_bin)
            self.m_result.append(XOR_result)

            m_bin = []
            c_bin = []
            XOR_result = []
        print("\n==================== FIM DA OPERAÇÃO XOR ======================\n")
        print(f"Matrix de resultado após operação XOR - bin:\n {self.m_result}\n")
    
    def Encrypt(self):
        #mod = 0
        self.bit_work()
    
        for index in range(self.tam):
            """ if int(self.m_result[index],2) < 32 or int(self.m_result[index],2) == 127:
                diff = 32 - (int(self.m_result[index],2))
                self.m_result[index] = int(self.m_result[index], 2) + (diff + self.key_sum% len(self.c_list))
                #mod += 1
            else:
                self.m_result[index] = int(self.m_result[index], 2) """
            self.m_result[index] = int(self.m_result[index], 2)

        print(f"\nMatrix de resultado após operação XOR - hex:\n {self.m_result}\n")

        for index in range(self.tam):
            self.m_result[index] = chr(self.m_result[index])

        print(f"\nMatrix de resultado após operação XOR - char:\n {self.m_result}\n")

        return ''.join(self.m_result)

    def Decrypt(self):
        pass
        
