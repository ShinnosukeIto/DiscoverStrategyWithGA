import random
import numpy as np

class GA:
  def __init__(self, Np, Ng, Pc, Pm, locus_num):
    self.Np = Np   #選出個体数(population number)
    self.Ng = Ng   #最大世代(generation number)
    self.Pc = Pc   #交叉率(probability of clossover)
    self.Pm = Pm   #突然変異率(probability of mutation)
    self.locus_num = locus_num  #遺伝子座
  
  def Solve(self, func):
    group = self.GenerateGroup(self.Np)
    self.fitnessfunc = func
    
    #最大世代数分計算
    for i in range(self.Ng):
      #個体ごとの適応度を計算
      evaluation = [self.GetFitness(individual) for individual in group]
      fitness = [e/sum(evaluation) for e in evaluation]
      #適応度比例選択によって親個体を選出
      candidate = [self.Selection(group, fitness) for j in range(self.Np)]
      #エリート(優秀個体)の選出
      elite = list(P[np.argmax(evaluation)])
      #新世代の個体群
      newgroup = list() 
      #親個体の選出
      while len(newgroup) != self.Np:
        #交叉のための親を選定
        parent1 = self.Selection(group, fitness)
        parent2 = self.Selection(group, fitness)
        #交叉もしくはコピーを作成
        children = list()
        if random.random() < self.Pc:
          children = self.UniformCrossOver(parent1, parent2)
        else:
          children.append(parent1)
          children.append(parent2)
        #突然変異を適用
        for child in children:
          self.Mutation(child)
          newgroup.append(child)
      evaluation = [self.GetFitness(individual) for individual in newgroup]
      newgroup[np.argmin(evaluation)] = elite
      P = list(newgroup)

  def GetFitness(self, individual):
    fitness = self.fitnessfunc(individual)
    return fitness
  
  def Mutation(self, individual):
    for i in range(self.locus_num*5):
      if random.random() < self.Pm:
        individual[i] = '1' if individual[i] == '0' else '0'

  def CrossOver(self, parent1, parent2):
    return self.UniformCrossOver(parent1, parent2)
  
  def UniformCrossOver(self, parent1, parent2):
    child1 = list()
    child2 = list()
    mask = [0 if random.random() < 0.5 else 1 for i in range(self.locus_num)]
    for i,mb in enumerate(mask):
      if mb == 1:
        child1.append(parent1[i])
        child2.append(parent1[i])
      else:
        child1.append(parent2[i])
        tmp = '0' if parent2[i] == '1' else '1'
        child2.append(tmp)
    return [child1, child2]
  
  def Selection(self, group, fitness):
    return self.FitnessProportionalSelection(group, fitness)
  
  def FitnessProportionalSelection(self, group, fitness):
    choiced_index = np.random.choice([i for i in range(len(group))], p=fitness)
    candidate = group[choiced_index]
    return candidate

  def GenerateGroup(self, individual_num):
    group = [self.GenerateIndividual() for i in range(individual_num)]
    return group

  def GenerateIndividual(self):
    individual = list()
    for i in range(self.locus_num):
      num_str = '0' if random.random() < 0.5 else '1'
      individual.append(num_str)
    return individual