# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:19:43 2018

@author: DLY
"""
#https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247487412&idx=1&sn=290e5b314e8e26e41f3e2dea39927990&chksm=9788987ba0ff116d18029e3b44ff5c59f6715801f19a18d02853f1e3b7d220cd9fbe8d6a3e8f&scene=0#rd
import hashlib
class Block:
    def __init__(self,data,prev_hash):
        self.previous_hash=prev_hash
        self.data=data
    
    @property #把一个方法变成属性
    def hash(self):
        message=hashlib.sha256()
        message.update(str(self.data).encode('utf-8'))
        return message.hexdigest()
    
def create_genesis_block():
    return Block(data='Genesis Block', prev_hash='')

class BlockChain:
    def __init__(self):
        self.blocks=[create_genesis_block()]
        
    def add_block(self,data):
        prev_block=self.blocks[len(self.blocks)-1]
        new_block=Block(data,prev_block.hash)
        self.blocks.append(new_block)
        return new_block
    
if __name__=='__main__':
    bc=BlockChain()
    b1=bc.add_block('jack send 1 BTC to Sam')
    b2=bc.add_block('Sam send 2 BTC to lili')
    
    for b in bc.blocks:
        print('Prev Hash:{}'.format(b.previous_hash))
        print('Data:{}'.format(b.data))
        print('Hash:{}'.format(b.hash))
        print('-'*100)