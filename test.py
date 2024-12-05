from simulations_functions import asyncSimulations_Linux
# from BHA_functions.datacollector import DataCollector
# from BHA_functions.graphic import GraphicGenerator
from BHA_functions import GraphicGenerator
from datetime import datetime

GRAPHIC_POINTS = 3
RUNS_PER_POINT = 10
CORES = 10

datacollectors = []
for i in range(0, GRAPHIC_POINTS):
    start = datetime.now()
    simulations_params = {
        'runs':RUNS_PER_POINT,
        'topology':'Ba',
        'number_nodes':20,
        'rows':4,
        'columns':3,
        'prob_edge_creation':0.1,
        'edges_to_attach':3,
        'entanglements_replanished':10,
        'requests':100,
        'attempts_per_request':2,
        'network_prob':0.8,
        'num_black_holes':2,
        'black_hole_prob':0.1,
        'black_hole_target':True
    }

    simulations_dc = asyncSimulations_Linux(cores=CORES, **simulations_params)
    datacollectors.append(simulations_dc)
    print(f"As {simulations_params['runs']} simulações finalizaram no tempo de: {datetime.now()-start}")

datacollectors = tuple(datacollectors)

graphicGen = GraphicGenerator(datacollectors)
keys = graphicGen.create_new_axis('Taxa de Sucesso')
print(keys)
graphicGen.add_on_plot('Taxa de Sucesso', 'teste 1', (0.2, 0.5, 0.1), "Success Tax")
graphicGen.show_plot('Taxa de Sucesso', "Taxa de Sucesso", 'Itensidade', "Taxa de sucesso")