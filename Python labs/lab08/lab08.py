import random
import math
import operator
from deap import base, creator, tools, gp

# Define protected division to handle division by zero
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

# Define the primitive sets
def create_primitive_set():
    pset = gp.PrimitiveSet("MAIN", arity=1)
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protectedDiv, 2)
    pset.addTerminal(1)  # Treat 'X' as 1
    return pset

# Define fitness evaluation function
def eval_fitness(individual):
    func = toolbox.compile(expr=individual)
    predicted_values = [func(x) for x in range(1, 11)]  # Assuming X ranges from 1 to 10
    actual_values = [5*x*3 - 6*x*2 + 8*x for x in range(1, 11)]
    rmse = math.sqrt(sum((p - a)**2 for p, a in zip(predicted_values, actual_values)) / len(predicted_values))
    return rmse,

# Create toolbox
def create_toolbox(pset):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)
    toolbox.register("evaluate", eval_fitness)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
    toolbox.register("select", tools.selTournament, tournsize=3)
    return toolbox

if _name_ == "_main_":
    pset = create_primitive_set()
    toolbox = create_toolbox(pset)

    random.seed(7)
    population = toolbox.population(n=500)
    prob_crossing, prob_mutating = 0.5, 0.2
    num_generations = 10

    print('\nEvolution process starts')

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    # Main evolution loop
    for g in range(num_generations):
        print("\n- Generation", g)
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < prob_crossing:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < prob_mutating:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Replace population with next generation individuals
        population[:] = offspring

        # Print statistics for the current generation
        fits = [ind.fitness.values[0] for ind in population]
        length = len(population)
        mean = sum(fits) / length
        std = math.sqrt(sum((fit - mean)**2 for fit in fits) / length)

        print('Min =', min(fits), ', Max =', max(fits))
        print('Average =', round(mean, 2), ', Standard deviation =', round(std, 2))

    print("\n- Evolution ends")
    best_ind = tools.selBest(population, 1)[0]
    print('\nBest individual:\n', best_ind)