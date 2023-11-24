import numpy as np

# magasság, tömeg, kor
np_baseball = np.array([[  74.  ,  180.  ,   22.99],
       [  74.  ,  215.  ,   34.69],
       [  72.  ,  210.  ,   30.78],
       [  72.  ,  210.  ,   35.43],
       [  73.  ,  188.  ,   35.71],
       [  69.  ,  176.  ,   29.39],
       [  69.  ,  209.  ,   30.77],
       [  71.  ,  200.  ,   35.07],
       [  76.  ,  231.  ,   30.19],
       [  71.  ,  180.  ,   27.05],
       [  73.  ,  188.  ,   23.88],
       [  73.  ,  180.  ,   26.96],
       [  74.  ,  185.  ,   23.29],
       [  74.  ,  160.  ,   26.11],
       [  69.  ,  180.  ,   27.55],
       [  70.  ,  185.  ,   34.27],
       [  73.  ,  189.  ,   27.99],
       [  75.  ,  185.  ,   22.38],
       [  78.  ,  219.  ,   22.89],
       [  79.  ,  230.  ,   25.76],
       [  76.  ,  205.  ,   36.33],
       [  74.  ,  230.  ,   31.17],
       [  76.  ,  195.  ,   32.31],
       [  72.  ,  180.  ,   31.03],
       [  71.  ,  192.  ,   29.26],
       [  75.  ,  225.  ,   29.47],
       [  77.  ,  203.  ,   32.46],
       [  74.  ,  195.  ,   35.67],
       [  73.  ,  182.  ,   25.89],
       [  74.  ,  188.  ,   26.55],
       [  78.  ,  200.  ,   24.17],
       [  73.  ,  180.  ,   26.69],
       [  75.  ,  200.  ,   25.13],
       [  73.  ,  200.  ,   27.9 ],
       [  75.  ,  245.  ,   30.17],
       [  75.  ,  240.  ,   31.36],
       [  74.  ,  215.  ,   30.99],
       [  69.  ,  185.  ,   32.24],
       [  71.  ,  175.  ,   27.61],
       [  74.  ,  199.  ,   28.2 ],
       [  73.  ,  200.  ,   28.85],
       [  73.  ,  215.  ,   24.21],
       [  76.  ,  200.  ,   22.02],
       [  74.  ,  205.  ,   24.97],
       [  74.  ,  206.  ,   26.78],
       [  70.  ,  186.  ,   32.51],
       [  72.  ,  188.  ,   30.95],
       [  77.  ,  220.  ,   33.09],
       [  74.  ,  210.  ,   32.74],
       [  70.  ,  195.  ,   30.69],
       [  73.  ,  200.  ,   23.45],
       [  75.  ,  200.  ,   24.94],
       [  76.  ,  212.  ,   24.09],
       [  76.  ,  224.  ,   35.23],
       [  78.  ,  210.  ,   27.43],
       [  74.  ,  205.  ,   30.6 ],
       [  74.  ,  220.  ,   27.94],
       [  76.  ,  195.  ,   29.99],
       [  77.  ,  200.  ,   25.17],
       [  81.  ,  260.  ,   24.13],
       [  78.  ,  228.  ,   30.46],
       [  75.  ,  270.  ,   25.96],
       [  77.  ,  200.  ,   22.55],
       [  75.  ,  210.  ,   26.29],
       [  76.  ,  190.  ,   24.79],
       [  74.  ,  220.  ,   31.74],
       [  72.  ,  180.  ,   23.92],
       [  72.  ,  205.  ,   25.33],
       [  75.  ,  210.  ,   24.02],
       [  73.  ,  220.  ,   23.7 ],
       [  73.  ,  211.  ,   31.59],
       [  73.  ,  200.  ,   29.95],
       [  70.  ,  180.  ,   23.64],
       [  70.  ,  190.  ,   32.33],
       [  70.  ,  170.  ,   23.13],
       [  76.  ,  230.  ,   26.6 ],
       [  68.  ,  155.  ,   26.46],
       [  71.  ,  185.  ,   25.75],
       [  72.  ,  185.  ,   27.51],
       [  75.  ,  200.  ,   25.11],
       [  75.  ,  225.  ,   32.51],
       [  75.  ,  225.  ,   34.67],
       [  75.  ,  220.  ,   31.06],
       [  68.  ,  160.  ,   29.1 ],
       [  74.  ,  205.  ,   28.66],
       [  78.  ,  235.  ,   28.35],
       [  71.  ,  250.  ,   33.77],
       [  73.  ,  210.  ,   30.89],
       [  76.  ,  190.  ,   37.74],
       [  74.  ,  160.  ,   24.14],
       [  74.  ,  200.  ,   25.71],
       [  79.  ,  205.  ,   24.41],
       [  75.  ,  222.  ,   24.32],
       [  73.  ,  195.  ,   28.09],
       [  76.  ,  205.  ,   33.31],
       [  74.  ,  220.  ,   36.4 ],
       [  74.  ,  220.  ,   37.36],
       [  73.  ,  170.  ,   31.61],
       [  72.  ,  185.  ,   25.14],
       [  74.  ,  195.  ,   30.29],
       [  73.  ,  220.  ,   36.37],
       [  74.  ,  230.  ,   34.89],
       [  72.  ,  180.  ,   23.79],
       [  73.  ,  220.  ,   27.96],
       [  69.  ,  180.  ,   23.54],
       [  72.  ,  180.  ,   31.37],
       [  73.  ,  170.  ,   31.29],
       [  75.  ,  210.  ,   33.01],
       [  75.  ,  215.  ,   25.1 ],
       [  73.  ,  200.  ,   31.28],
       [  72.  ,  213.  ,   34.75],
       [  72.  ,  180.  ,   23.46],
       [  76.  ,  192.  ,   25.37],
       [  74.  ,  235.  ,   29.57],
       [  72.  ,  185.  ,   27.33],
       [  77.  ,  235.  ,   40.29],
       [  74.  ,  210.  ,   40.58],
       [  77.  ,  222.  ,   26.79],
       [  75.  ,  210.  ,   32.55],
       [  76.  ,  230.  ,   26.27],
       [  80.  ,  220.  ,   29.47],
       [  74.  ,  180.  ,   29.07],
       [  74.  ,  190.  ,   23.15],
       [  75.  ,  200.  ,   24.9 ],
       [  78.  ,  210.  ,   23.29],
       [  73.  ,  194.  ,   31.18],
       [  73.  ,  180.  ,   26.56],
       [  74.  ,  190.  ,   25.03],
       [  75.  ,  240.  ,   35.66],
       [  76.  ,  200.  ,   29.64],
       [  71.  ,  198.  ,   30.74],
       [  73.  ,  200.  ,   28.43],
       [  74.  ,  195.  ,   33.77],
       [  76.  ,  210.  ,   40.97],
       [  76.  ,  220.  ,   23.52],
       [  74.  ,  190.  ,   28.19],
       [  73.  ,  210.  ,   26.84],
       [  74.  ,  225.  ,   26.16],
       [  70.  ,  180.  ,   28.67],
       [  72.  ,  185.  ,   24.2 ],
       [  73.  ,  170.  ,   27.08],
       [  73.  ,  185.  ,   24.76],
       [  73.  ,  185.  ,   23.36],
       [  73.  ,  180.  ,   25.35],
       [  71.  ,  178.  ,   24.63],
       [  74.  ,  175.  ,   24.02],
       [  74.  ,  200.  ,   24.58],
       [  72.  ,  204.  ,   30.82],
       [  74.  ,  211.  ,   32.89],
       [  71.  ,  190.  ,   33.33],
       [  74.  ,  210.  ,   33.52],
       [  73.  ,  190.  ,   36.24],
       [  75.  ,  190.  ,   28.5 ],
       [  75.  ,  185.  ,   29.42],
       [  79.  ,  290.  ,   26.61],
       [  73.  ,  175.  ,   23.79],
       [  75.  ,  185.  ,   24.96],
       [  76.  ,  200.  ,   25.93],
       [  74.  ,  220.  ,   22.81],
       [  76.  ,  170.  ,   25.29],
       [  78.  ,  220.  ,   26.07],
       [  74.  ,  190.  ,   26.09],
       [  76.  ,  220.  ,   23.23],
       [  72.  ,  205.  ,   33.49],
       [  74.  ,  200.  ,   31.84],
       [  76.  ,  250.  ,   42.3 ],
       [  74.  ,  225.  ,   35.82],
       [  75.  ,  215.  ,   35.27],
       [  78.  ,  210.  ,   26.81],
       [  75.  ,  215.  ,   38.49],
       [  72.  ,  195.  ,   32.68],
       [  74.  ,  200.  ,   34.93],
       [  72.  ,  194.  ,   26.26],
       [  74.  ,  220.  ,   27.56],
       [  70.  ,  180.  ,   23.98],
       [  71.  ,  180.  ,   29.73],
       [  70.  ,  170.  ,   31.33],
       [  75.  ,  195.  ,   27.13],
       [  71.  ,  180.  ,   26.75],
       [  71.  ,  170.  ,   27.09],
       [  73.  ,  206.  ,   29.23],
       [  72.  ,  205.  ,   28.88],
       [  71.  ,  200.  ,   33.01],
       [  73.  ,  225.  ,   30.57],
       [  72.  ,  201.  ,   31.24],
       [  75.  ,  225.  ,   24.95],
       [  74.  ,  233.  ,   24.62],
       [  74.  ,  180.  ,   24.98],
       [  75.  ,  225.  ,   26.22],
       [  73.  ,  180.  ,   26.04],
       [  77.  ,  220.  ,   26.45],
       [  73.  ,  180.  ,   25.25],
       [  76.  ,  237.  ,   27.77],
       [  75.  ,  215.  ,   35.16],
       [  74.  ,  190.  ,   37.1 ],
       [  76.  ,  235.  ,   34.51],
       [  75.  ,  190.  ,   29.28],
       [  73.  ,  180.  ,   32.14],
       [  71.  ,  165.  ,   23.94],
       [  76.  ,  195.  ,   27.45],
       [  75.  ,  200.  ,   28.77],
       [  72.  ,  190.  ,   23.58],
       [  71.  ,  190.  ,   27.56],
       [  77.  ,  185.  ,   24.01],
       [  73.  ,  185.  ,   26.52],
       [  74.  ,  205.  ,   35.54],
       [  71.  ,  190.  ,   29.43],
       [  72.  ,  205.  ,   29.9 ],
       [  74.  ,  206.  ,   32.7 ],
       [  75.  ,  220.  ,   28.8 ],
       [  73.  ,  208.  ,   32.82],
       [  72.  ,  170.  ,   24.36],
       [  75.  ,  195.  ,   32.68],
       [  75.  ,  210.  ,   31.59],
       [  74.  ,  190.  ,   33.32],
       [  72.  ,  211.  ,   32.97],
       [  74.  ,  230.  ,   32.72],
       [  71.  ,  170.  ,   22.55],
       [  70.  ,  185.  ,   27.45],
       [  74.  ,  185.  ,   38.23],
       [  77.  ,  241.  ,   31.14],
       [  77.  ,  225.  ,   34.71],
       [  75.  ,  210.  ,   26.13],
       [  75.  ,  175.  ,   24.43],
       [  78.  ,  230.  ,   23.76],
       [  75.  ,  200.  ,   26.92],
       [  76.  ,  215.  ,   25.85],
       [  73.  ,  198.  ,   30.16],
       [  75.  ,  226.  ,   25.03],
       [  75.  ,  278.  ,   24.21],
       [  79.  ,  215.  ,   26.51],
       [  77.  ,  230.  ,   26.36],
       [  76.  ,  240.  ,   30.88],
       [  71.  ,  184.  ,   32.57],
       [  75.  ,  219.  ,   37.68],
       [  74.  ,  170.  ,   37.25],
       [  69.  ,  218.  ,   35.25],
       [  71.  ,  190.  ,   33.95],
       [  76.  ,  225.  ,   32.66],
       [  72.  ,  220.  ,   26.68],
       [  72.  ,  176.  ,   25.18],
       [  70.  ,  190.  ,   31.39],
       [  72.  ,  197.  ,   33.74],
       [  73.  ,  204.  ,   31.42],
       [  71.  ,  167.  ,   27.5 ],
       [  72.  ,  180.  ,   24.25],
       [  71.  ,  195.  ,   29.78],
       [  73.  ,  220.  ,   30.  ],
       [  72.  ,  215.  ,   33.09],
       [  73.  ,  185.  ,   25.96],
       [  74.  ,  190.  ,   23.34],
       [  74.  ,  205.  ,   29.98],
       [  72.  ,  205.  ,   38.28],
       [  75.  ,  200.  ,   24.97],
       [  74.  ,  210.  ,   24.34],
       [  74.  ,  215.  ,   29.49],
       [  77.  ,  200.  ,   24.02],
       [  75.  ,  205.  ,   24.73],
       [  73.  ,  211.  ,   42.3 ],
       [  72.  ,  190.  ,   29.54],
       [  71.  ,  208.  ,   29.95],
       [  74.  ,  200.  ,   29.24],
       [  77.  ,  210.  ,   30.3 ],
       [  75.  ,  232.  ,   40.77],
       [  75.  ,  230.  ,   38.85],
       [  75.  ,  210.  ,   22.31],
       [  78.  ,  220.  ,   25.44],
       [  78.  ,  210.  ,   21.78],
       [  74.  ,  202.  ,   22.64],
       [  76.  ,  212.  ,   26.11],
       [  78.  ,  225.  ,   27.55],
       [  76.  ,  170.  ,   24.63],
       [  70.  ,  190.  ,   23.58],
       [  72.  ,  200.  ,   30.73],
       [  80.  ,  237.  ,   32.17],
       [  74.  ,  220.  ,   30.43],
       [  74.  ,  170.  ,   23.27],
       [  71.  ,  193.  ,   32.51],
       [  70.  ,  190.  ,   25.08],
       [  72.  ,  150.  ,   22.41],
       [  71.  ,  220.  ,   27.9 ],
       [  74.  ,  200.  ,   34.74],
       [  71.  ,  190.  ,   30.79],
       [  72.  ,  185.  ,   25.71],
       [  71.  ,  185.  ,   29.26],
       [  74.  ,  200.  ,   21.58],
       [  69.  ,  172.  ,   33.36],
       [  76.  ,  220.  ,   24.94],
       [  75.  ,  225.  ,   20.9 ],
       [  75.  ,  190.  ,   21.52],
       [  76.  ,  195.  ,   25.85],
       [  73.  ,  219.  ,   27.27],
       [  76.  ,  190.  ,   26.75],
       [  73.  ,  197.  ,   36.03],
       [  77.  ,  200.  ,   30.52],
       [  73.  ,  195.  ,   32.55],
       [  72.  ,  210.  ,   29.86],
       [  72.  ,  177.  ,   29.58],
       [  77.  ,  220.  ,   30.02],
       [  77.  ,  235.  ,   29.16],
       [  71.  ,  180.  ,   22.3 ],
       [  74.  ,  195.  ,   22.06],
       [  74.  ,  195.  ,   25.65],
       [  73.  ,  190.  ,   25.49],
       [  78.  ,  230.  ,   27.86],
       [  75.  ,  190.  ,   23.73],
       [  73.  ,  200.  ,   31.78],
       [  70.  ,  190.  ,   23.06],
       [  74.  ,  190.  ,   26.6 ],
       [  72.  ,  200.  ,   29.39],
       [  73.  ,  200.  ,   26.51],
       [  73.  ,  184.  ,   25.08],
       [  75.  ,  200.  ,   25.76],
       [  75.  ,  180.  ,   22.52],
       [  74.  ,  219.  ,   25.57],
       [  76.  ,  187.  ,   25.43],
       [  73.  ,  200.  ,   34.65],
       [  74.  ,  220.  ,   22.68],
       [  75.  ,  205.  ,   21.46],
       [  75.  ,  190.  ,   23.47],
       [  72.  ,  170.  ,   23.1 ],
       [  73.  ,  160.  ,   29.14],
       [  73.  ,  215.  ,   29.77],
       [  72.  ,  175.  ,   23.85],
       [  74.  ,  205.  ,   28.88],
       [  78.  ,  200.  ,   24.49],
       [  76.  ,  214.  ,   25.19],
       [  73.  ,  200.  ,   27.48],
       [  74.  ,  190.  ,   28.31],
       [  75.  ,  180.  ,   26.54],
       [  70.  ,  205.  ,   26.77],
       [  75.  ,  220.  ,   23.75],
       [  71.  ,  190.  ,   26.41],
       [  72.  ,  215.  ,   36.47],
       [  78.  ,  235.  ,   26.06],
       [  75.  ,  191.  ,   27.55],
       [  73.  ,  200.  ,   31.28],
       [  73.  ,  181.  ,   29.04],
       [  71.  ,  200.  ,   32.95],
       [  75.  ,  210.  ,   26.65],
       [  77.  ,  240.  ,   27.5 ],
       [  72.  ,  185.  ,   30.9 ],
       [  69.  ,  165.  ,   29.09],
       [  73.  ,  190.  ,   36.67],
       [  74.  ,  185.  ,   23.44],
       [  72.  ,  175.  ,   29.09],
       [  70.  ,  155.  ,   22.89],
       [  75.  ,  210.  ,   25.48],
       [  70.  ,  170.  ,   25.84],
       [  72.  ,  175.  ,   27.2 ],
       [  72.  ,  220.  ,   25.22],
       [  74.  ,  210.  ,   24.67],
       [  73.  ,  205.  ,   39.25],
       [  74.  ,  200.  ,   32.17],
       [  76.  ,  205.  ,   32.77],
       [  75.  ,  195.  ,   29.83],
       [  80.  ,  240.  ,   31.02],
       [  72.  ,  150.  ,   29.73],
       [  75.  ,  200.  ,   28.48],
       [  73.  ,  215.  ,   26.51],
       [  74.  ,  202.  ,   26.  ],
       [  74.  ,  200.  ,   23.36],
       [  73.  ,  190.  ,   25.9 ],
       [  75.  ,  205.  ,   28.5 ],
       [  75.  ,  190.  ,   25.62],
       [  71.  ,  160.  ,   30.94],
       [  73.  ,  215.  ,   26.59],
       [  75.  ,  185.  ,   22.78],
       [  74.  ,  200.  ,   32.26],
       [  74.  ,  190.  ,   30.35],
       [  72.  ,  210.  ,   33.26],
       [  74.  ,  185.  ,   32.35],
       [  74.  ,  220.  ,   27.3 ],
       [  74.  ,  190.  ,   32.08],
       [  73.  ,  202.  ,   25.25],
       [  76.  ,  205.  ,   25.03],
       [  75.  ,  220.  ,   26.89],
       [  72.  ,  175.  ,   24.69],
       [  73.  ,  160.  ,   22.44],
       [  73.  ,  190.  ,   30.36],
       [  73.  ,  200.  ,   26.27],
       [  72.  ,  229.  ,   29.5 ],
       [  72.  ,  206.  ,   29.75],
       [  72.  ,  220.  ,   38.3 ],
       [  72.  ,  180.  ,   39.75],
       [  71.  ,  195.  ,   32.84],
       [  75.  ,  175.  ,   26.66],
       [  75.  ,  188.  ,   24.94],
       [  74.  ,  230.  ,   27.76],
       [  73.  ,  190.  ,   23.66],
       [  75.  ,  200.  ,   24.96],
       [  79.  ,  190.  ,   23.65],
       [  74.  ,  219.  ,   29.42],
       [  76.  ,  235.  ,   32.18],
       [  73.  ,  180.  ,   26.66],
       [  74.  ,  180.  ,   27.47],
       [  74.  ,  180.  ,   25.66],
       [  72.  ,  200.  ,   35.13],
       [  74.  ,  234.  ,   31.15],
       [  74.  ,  185.  ,   35.67],
       [  75.  ,  220.  ,   29.6 ],
       [  78.  ,  223.  ,   30.14],
       [  74.  ,  200.  ,   24.53],
       [  74.  ,  210.  ,   24.49],
       [  74.  ,  200.  ,   26.28],
       [  77.  ,  210.  ,   24.06],
       [  70.  ,  190.  ,   35.88],
       [  73.  ,  177.  ,   30.42],
       [  74.  ,  227.  ,   30.09],
       [  73.  ,  180.  ,   26.5 ],
       [  71.  ,  195.  ,   24.94],
       [  75.  ,  199.  ,   29.6 ],
       [  71.  ,  175.  ,   32.43],
       [  72.  ,  185.  ,   37.16],
       [  77.  ,  240.  ,   30.57],
       [  74.  ,  210.  ,   27.01],
       [  70.  ,  180.  ,   30.23],
       [  77.  ,  194.  ,   26.03],
       [  73.  ,  225.  ,   28.23],
       [  72.  ,  180.  ,   25.21],
       [  76.  ,  205.  ,   25.45],
       [  71.  ,  193.  ,   26.24],
       [  76.  ,  230.  ,   30.15],
       [  78.  ,  230.  ,   29.8 ],
       [  75.  ,  220.  ,   33.41],
       [  73.  ,  200.  ,   30.95],
       [  78.  ,  249.  ,   31.17],
       [  74.  ,  190.  ,   30.95],
       [  79.  ,  208.  ,   29.44],
       [  75.  ,  245.  ,   27.14],
       [  76.  ,  250.  ,   26.21],
       [  72.  ,  160.  ,   24.08],
       [  75.  ,  192.  ,   23.96],
       [  75.  ,  220.  ,   24.94],
       [  70.  ,  170.  ,   29.56],
       [  72.  ,  197.  ,   26.42],
       [  70.  ,  155.  ,   23.92],
       [  74.  ,  190.  ,   25.23],
       [  71.  ,  200.  ,   35.82],
       [  76.  ,  220.  ,   23.87],
       [  73.  ,  210.  ,   32.57],
       [  76.  ,  228.  ,   25.79],
       [  71.  ,  190.  ,   31.47],
       [  69.  ,  160.  ,   22.61],
       [  72.  ,  184.  ,   24.85],
       [  72.  ,  180.  ,   27.33],
       [  69.  ,  180.  ,   26.67],
       [  73.  ,  200.  ,   37.43],
       [  69.  ,  176.  ,   29.31],
       [  73.  ,  160.  ,   29.85],
       [  74.  ,  222.  ,   27.93],
       [  74.  ,  211.  ,   31.62],
       [  72.  ,  195.  ,   30.55],
       [  71.  ,  200.  ,   24.77],
       [  72.  ,  175.  ,   33.77],
       [  72.  ,  206.  ,   27.97],
       [  76.  ,  240.  ,   27.85],
       [  76.  ,  185.  ,   23.26],
       [  76.  ,  260.  ,   25.38],
       [  74.  ,  185.  ,   23.35],
       [  76.  ,  221.  ,   25.45],
       [  75.  ,  205.  ,   26.49],
       [  71.  ,  200.  ,   24.  ],
       [  72.  ,  170.  ,   24.16],
       [  71.  ,  201.  ,   28.1 ],
       [  73.  ,  205.  ,   25.65],
       [  75.  ,  185.  ,   28.58],
       [  76.  ,  205.  ,   32.27],
       [  75.  ,  245.  ,   29.86],
       [  71.  ,  220.  ,   25.14],
       [  75.  ,  210.  ,   23.03],
       [  74.  ,  220.  ,   30.25],
       [  72.  ,  185.  ,   30.67],
       [  73.  ,  175.  ,   27.73],
       [  73.  ,  170.  ,   23.34],
       [  73.  ,  180.  ,   25.94],
       [  73.  ,  200.  ,   31.56],
       [  76.  ,  210.  ,   34.85],
       [  72.  ,  175.  ,   23.98],
       [  76.  ,  220.  ,   23.14],
       [  73.  ,  206.  ,   28.99],
       [  73.  ,  180.  ,   25.02],
       [  73.  ,  210.  ,   29.85],
       [  75.  ,  195.  ,   27.03],
       [  75.  ,  200.  ,   25.15],
       [  77.  ,  200.  ,   27.12],
       [  73.  ,  164.  ,   31.63],
       [  72.  ,  180.  ,   32.62],
       [  75.  ,  220.  ,   39.79],
       [  70.  ,  195.  ,   34.47],
       [  74.  ,  205.  ,   23.47],
       [  72.  ,  170.  ,   25.31],
       [  80.  ,  240.  ,   27.1 ],
       [  71.  ,  210.  ,   24.35],
       [  71.  ,  195.  ,   23.45],
       [  74.  ,  200.  ,   28.24],
       [  74.  ,  205.  ,   28.77],
       [  73.  ,  192.  ,   26.53],
       [  75.  ,  190.  ,   25.64],
       [  76.  ,  170.  ,   25.83],
       [  73.  ,  240.  ,   38.06],
       [  77.  ,  200.  ,   36.38],
       [  72.  ,  205.  ,   25.27],
       [  73.  ,  175.  ,   27.2 ],
       [  77.  ,  250.  ,   31.59],
       [  76.  ,  220.  ,   29.56],
       [  71.  ,  224.  ,   35.5 ],
       [  75.  ,  210.  ,   30.35],
       [  73.  ,  195.  ,   24.11],
       [  74.  ,  180.  ,   23.29],
       [  77.  ,  245.  ,   31.48],
       [  71.  ,  175.  ,   27.23],
       [  72.  ,  180.  ,   24.07],
       [  73.  ,  215.  ,   28.68],
       [  69.  ,  175.  ,   27.05],
       [  73.  ,  180.  ,   31.15],
       [  70.  ,  195.  ,   31.85],
       [  74.  ,  230.  ,   31.68],
       [  76.  ,  230.  ,   34.23],
       [  73.  ,  205.  ,   32.01],
       [  73.  ,  215.  ,   25.41],
       [  75.  ,  195.  ,   24.73],
       [  73.  ,  180.  ,   25.66],
       [  79.  ,  205.  ,   24.5 ],
       [  74.  ,  180.  ,   24.38],
       [  73.  ,  190.  ,   26.89],
       [  74.  ,  180.  ,   24.2 ],
       [  77.  ,  190.  ,   26.97],
       [  75.  ,  190.  ,   25.21],
       [  74.  ,  220.  ,   30.46],
       [  73.  ,  210.  ,   28.53],
       [  77.  ,  255.  ,   25.75],
       [  73.  ,  190.  ,   31.15],
       [  77.  ,  230.  ,   26.48],
       [  74.  ,  200.  ,   26.93],
       [  74.  ,  205.  ,   29.55],
       [  73.  ,  210.  ,   34.75],
       [  77.  ,  225.  ,   29.71],
       [  74.  ,  215.  ,   29.83],
       [  77.  ,  220.  ,   33.57],
       [  75.  ,  205.  ,   28.21],
       [  77.  ,  200.  ,   27.54],
       [  75.  ,  220.  ,   26.05],
       [  71.  ,  197.  ,   23.64],
       [  74.  ,  225.  ,   24.82],
       [  70.  ,  187.  ,   29.8 ],
       [  79.  ,  245.  ,   34.71],
       [  72.  ,  185.  ,   29.22],
       [  72.  ,  185.  ,   23.96],
       [  70.  ,  175.  ,   23.87],
       [  74.  ,  200.  ,   26.77],
       [  74.  ,  180.  ,   23.49],
       [  72.  ,  188.  ,   26.77],
       [  73.  ,  225.  ,   24.51],
       [  72.  ,  200.  ,   33.23],
       [  74.  ,  210.  ,   31.04],
       [  74.  ,  245.  ,   32.02],
       [  76.  ,  213.  ,   31.44],
       [  82.  ,  231.  ,   43.47],
       [  74.  ,  165.  ,   28.38],
       [  74.  ,  228.  ,   27.81],
       [  70.  ,  210.  ,   24.57],
       [  73.  ,  250.  ,   23.34],
       [  73.  ,  191.  ,   27.09],
       [  74.  ,  190.  ,   25.14],
       [  77.  ,  200.  ,   27.07],
       [  72.  ,  215.  ,   24.02],
       [  76.  ,  254.  ,   27.6 ],
       [  73.  ,  232.  ,   27.99],
       [  73.  ,  180.  ,   27.56],
       [  72.  ,  215.  ,   28.63],
       [  74.  ,  220.  ,   30.99],
       [  74.  ,  180.  ,   26.33],
       [  71.  ,  200.  ,   26.97],
       [  72.  ,  170.  ,   22.85],
       [  75.  ,  195.  ,   23.19],
       [  74.  ,  210.  ,   23.87],
       [  74.  ,  200.  ,   33.98],
       [  77.  ,  220.  ,   28.26],
       [  70.  ,  165.  ,   29.12],
       [  71.  ,  180.  ,   26.18],
       [  73.  ,  200.  ,   28.03],
       [  76.  ,  200.  ,   23.08],
       [  71.  ,  170.  ,   26.24],
       [  75.  ,  224.  ,   26.63],
       [  74.  ,  220.  ,   24.21],
       [  72.  ,  180.  ,   23.01],
       [  76.  ,  198.  ,   23.13],
       [  79.  ,  240.  ,   23.08],
       [  76.  ,  239.  ,   25.13],
       [  73.  ,  185.  ,   24.66],
       [  76.  ,  210.  ,   26.03],
       [  78.  ,  220.  ,   28.7 ],
       [  75.  ,  200.  ,   25.57],
       [  76.  ,  195.  ,   24.65],
       [  72.  ,  220.  ,   25.55],
       [  72.  ,  230.  ,   22.27],
       [  73.  ,  170.  ,   24.76],
       [  73.  ,  220.  ,   23.98],
       [  75.  ,  230.  ,   27.85],
       [  71.  ,  165.  ,   22.14],
       [  76.  ,  205.  ,   27.05],
       [  70.  ,  192.  ,   31.45],
       [  75.  ,  210.  ,   32.03],
       [  74.  ,  205.  ,   29.95],
       [  75.  ,  200.  ,   23.47],
       [  73.  ,  210.  ,   37.21],
       [  71.  ,  185.  ,   25.67],
       [  71.  ,  195.  ,   34.69],
       [  72.  ,  202.  ,   30.04],
       [  73.  ,  205.  ,   32.52],
       [  73.  ,  195.  ,   24.15],
       [  72.  ,  180.  ,   26.86],
       [  69.  ,  200.  ,   27.94],
       [  73.  ,  185.  ,   26.63],
       [  78.  ,  240.  ,   27.31],
       [  71.  ,  185.  ,   30.55],
       [  73.  ,  220.  ,   40.68],
       [  75.  ,  205.  ,   37.27],
       [  76.  ,  205.  ,   25.78],
       [  70.  ,  180.  ,   30.98],
       [  74.  ,  201.  ,   28.41],
       [  77.  ,  190.  ,   30.01],
       [  75.  ,  208.  ,   31.57],
       [  79.  ,  240.  ,   28.81],
       [  72.  ,  180.  ,   24.09],
       [  77.  ,  230.  ,   26.47],
       [  73.  ,  195.  ,   30.5 ],
       [  75.  ,  215.  ,   23.74],
       [  75.  ,  190.  ,   24.49],
       [  75.  ,  195.  ,   26.73],
       [  73.  ,  215.  ,   27.01],
       [  73.  ,  215.  ,   39.75],
       [  76.  ,  220.  ,   27.16],
       [  77.  ,  220.  ,   25.74],
       [  75.  ,  230.  ,   37.43],
       [  70.  ,  195.  ,   39.85],
       [  71.  ,  190.  ,   28.62],
       [  71.  ,  195.  ,   23.9 ],
       [  75.  ,  209.  ,   25.18],
       [  74.  ,  204.  ,   33.53],
       [  69.  ,  170.  ,   33.03],
       [  70.  ,  185.  ,   31.35],
       [  75.  ,  205.  ,   22.39],
       [  72.  ,  175.  ,   27.99],
       [  75.  ,  210.  ,   27.22],
       [  73.  ,  190.  ,   27.49],
       [  72.  ,  180.  ,   27.53],
       [  72.  ,  180.  ,   26.26],
       [  72.  ,  160.  ,   25.18],
       [  76.  ,  235.  ,   27.12],
       [  75.  ,  200.  ,   27.69],
       [  74.  ,  210.  ,   25.69],
       [  69.  ,  180.  ,   28.11],
       [  73.  ,  190.  ,   31.21],
       [  72.  ,  197.  ,   30.8 ],
       [  72.  ,  203.  ,   30.21],
       [  75.  ,  205.  ,   28.06],
       [  77.  ,  170.  ,   26.52],
       [  76.  ,  200.  ,   23.1 ],
       [  80.  ,  250.  ,   25.02],
       [  77.  ,  200.  ,   26.14],
       [  76.  ,  220.  ,   25.38],
       [  79.  ,  200.  ,   27.6 ],
       [  71.  ,  190.  ,   25.5 ],
       [  75.  ,  170.  ,   24.24],
       [  73.  ,  190.  ,   23.32],
       [  76.  ,  220.  ,   31.56],
       [  77.  ,  215.  ,   34.19],
       [  73.  ,  206.  ,   36.78],
       [  76.  ,  215.  ,   27.73],
       [  70.  ,  185.  ,   34.88],
       [  75.  ,  235.  ,   31.  ],
       [  73.  ,  188.  ,   48.52],
       [  75.  ,  230.  ,   34.68],
       [  70.  ,  195.  ,   37.38],
       [  69.  ,  168.  ,   24.33],
       [  71.  ,  190.  ,   37.3 ],
       [  72.  ,  160.  ,   23.72],
       [  72.  ,  200.  ,   24.19],
       [  73.  ,  200.  ,   25.7 ],
       [  70.  ,  189.  ,   29.06],
       [  70.  ,  180.  ,   33.48],
       [  73.  ,  190.  ,   29.85],
       [  76.  ,  200.  ,   34.3 ],
       [  75.  ,  220.  ,   40.66],
       [  72.  ,  187.  ,   21.9 ],
       [  73.  ,  240.  ,   27.39],
       [  79.  ,  190.  ,   23.13],
       [  71.  ,  180.  ,   35.35],
       [  72.  ,  185.  ,   40.93],
       [  74.  ,  210.  ,   33.67],
       [  74.  ,  220.  ,   37.39],
       [  74.  ,  219.  ,   27.97],
       [  72.  ,  190.  ,   25.54],
       [  76.  ,  193.  ,   25.81],
       [  76.  ,  175.  ,   22.53],
       [  72.  ,  180.  ,   22.86],
       [  72.  ,  215.  ,   24.07],
       [  71.  ,  210.  ,   29.5 ],
       [  72.  ,  200.  ,   30.03],
       [  72.  ,  190.  ,   27.38],
       [  70.  ,  185.  ,   30.51],
       [  77.  ,  220.  ,   28.3 ],
       [  74.  ,  170.  ,   29.84],
       [  72.  ,  195.  ,   33.41],
       [  76.  ,  205.  ,   33.6 ],
       [  71.  ,  195.  ,   35.6 ],
       [  76.  ,  210.  ,   24.19],
       [  71.  ,  190.  ,   37.88],
       [  73.  ,  190.  ,   27.56],
       [  70.  ,  180.  ,   24.42],
       [  73.  ,  220.  ,   31.05],
       [  73.  ,  190.  ,   31.56],
       [  72.  ,  186.  ,   35.55],
       [  71.  ,  185.  ,   41.21],
       [  71.  ,  190.  ,   27.12],
       [  71.  ,  180.  ,   26.97],
       [  72.  ,  190.  ,   28.92],
       [  72.  ,  170.  ,   30.06],
       [  74.  ,  210.  ,   31.51],
       [  74.  ,  240.  ,   30.69],
       [  74.  ,  220.  ,   30.19],
       [  71.  ,  180.  ,   38.11],
       [  72.  ,  210.  ,   28.68],
       [  75.  ,  210.  ,   27.44],
       [  72.  ,  195.  ,   24.63],
       [  71.  ,  160.  ,   28.11],
       [  72.  ,  180.  ,   28.9 ],
       [  72.  ,  205.  ,   24.11],
       [  72.  ,  200.  ,   40.53],
       [  72.  ,  185.  ,   29.5 ],
       [  74.  ,  245.  ,   28.62],
       [  74.  ,  190.  ,   26.42],
       [  77.  ,  210.  ,   30.18],
       [  75.  ,  200.  ,   33.75],
       [  73.  ,  200.  ,   30.06],
       [  75.  ,  222.  ,   29.22],
       [  73.  ,  215.  ,   24.47],
       [  76.  ,  240.  ,   24.94],
       [  72.  ,  170.  ,   28.77],
       [  77.  ,  220.  ,   28.54],
       [  75.  ,  156.  ,   27.32],
       [  72.  ,  190.  ,   35.12],
       [  71.  ,  202.  ,   24.04],
       [  71.  ,  221.  ,   36.39],
       [  75.  ,  200.  ,   22.81],
       [  72.  ,  190.  ,   33.6 ],
       [  73.  ,  210.  ,   38.98],
       [  73.  ,  190.  ,   34.39],
       [  71.  ,  200.  ,   33.15],
       [  70.  ,  165.  ,   29.35],
       [  75.  ,  190.  ,   26.59],
       [  71.  ,  185.  ,   23.46],
       [  76.  ,  230.  ,   22.43],
       [  73.  ,  208.  ,   24.89],
       [  68.  ,  209.  ,   24.67],
       [  71.  ,  175.  ,   26.17],
       [  72.  ,  180.  ,   29.54],
       [  74.  ,  200.  ,   39.49],
       [  77.  ,  205.  ,   34.08],
       [  72.  ,  200.  ,   30.52],
       [  76.  ,  250.  ,   28.77],
       [  78.  ,  210.  ,   33.75],
       [  81.  ,  230.  ,   32.69],
       [  72.  ,  244.  ,   22.59],
       [  73.  ,  202.  ,   37.04],
       [  76.  ,  240.  ,   22.7 ],
       [  72.  ,  200.  ,   25.6 ],
       [  72.  ,  215.  ,   27.23],
       [  74.  ,  177.  ,   25.74],
       [  76.  ,  210.  ,   30.29],
       [  73.  ,  170.  ,   26.72],
       [  76.  ,  215.  ,   33.9 ],
       [  75.  ,  217.  ,   29.86],
       [  70.  ,  198.  ,   36.13],
       [  71.  ,  200.  ,   27.54],
       [  74.  ,  220.  ,   31.49],
       [  72.  ,  170.  ,   28.1 ],
       [  73.  ,  200.  ,   34.07],
       [  76.  ,  230.  ,   27.28],
       [  76.  ,  231.  ,   30.8 ],
       [  73.  ,  183.  ,   28.2 ],
       [  71.  ,  192.  ,   27.9 ],
       [  68.  ,  167.  ,   28.26],
       [  71.  ,  190.  ,   30.96],
       [  71.  ,  180.  ,   24.18],
       [  74.  ,  180.  ,   27.52],
       [  77.  ,  215.  ,   27.78],
       [  69.  ,  160.  ,   26.25],
       [  72.  ,  205.  ,   29.5 ],
       [  76.  ,  223.  ,   30.39],
       [  75.  ,  175.  ,   23.18],
       [  76.  ,  170.  ,   25.81],
       [  75.  ,  190.  ,   23.01],
       [  76.  ,  240.  ,   31.72],
       [  72.  ,  175.  ,   44.28],
       [  74.  ,  230.  ,   36.91],
       [  76.  ,  223.  ,   26.54],
       [  74.  ,  196.  ,   29.27],
       [  72.  ,  167.  ,   30.51],
       [  75.  ,  195.  ,   31.28],
       [  78.  ,  190.  ,   26.51],
       [  77.  ,  250.  ,   34.87],
       [  70.  ,  190.  ,   39.28],
       [  72.  ,  190.  ,   28.56],
       [  79.  ,  190.  ,   27.82],
       [  74.  ,  170.  ,   25.94],
       [  71.  ,  160.  ,   28.53],
       [  68.  ,  150.  ,   22.11],
       [  77.  ,  225.  ,   27.71],
       [  75.  ,  220.  ,   37.38],
       [  71.  ,  209.  ,   30.67],
       [  72.  ,  210.  ,   30.48],
       [  70.  ,  176.  ,   27.12],
       [  72.  ,  260.  ,   22.81],
       [  72.  ,  195.  ,   24.46],
       [  73.  ,  190.  ,   34.73],
       [  72.  ,  184.  ,   36.53],
       [  74.  ,  180.  ,   24.53],
       [  72.  ,  195.  ,   27.17],
       [  72.  ,  195.  ,   26.9 ],
       [  75.  ,  219.  ,   33.67],
       [  72.  ,  225.  ,   29.14],
       [  73.  ,  212.  ,   32.61],
       [  74.  ,  202.  ,   33.87],
       [  72.  ,  185.  ,   24.41],
       [  78.  ,  200.  ,   24.94],
       [  75.  ,  209.  ,   27.36],
       [  72.  ,  200.  ,   26.33],
       [  74.  ,  195.  ,   25.72],
       [  75.  ,  228.  ,   28.7 ],
       [  75.  ,  210.  ,   28.53],
       [  76.  ,  190.  ,   26.07],
       [  74.  ,  212.  ,   27.31],
       [  74.  ,  190.  ,   23.26],
       [  73.  ,  218.  ,   28.62],
       [  74.  ,  220.  ,   32.16],
       [  71.  ,  190.  ,   38.43],
       [  74.  ,  235.  ,   31.81],
       [  75.  ,  210.  ,   29.1 ],
       [  76.  ,  200.  ,   31.28],
       [  74.  ,  188.  ,   29.17],
       [  76.  ,  210.  ,   25.89],
       [  76.  ,  235.  ,   26.13],
       [  73.  ,  188.  ,   29.13],
       [  75.  ,  215.  ,   28.92],
       [  75.  ,  216.  ,   26.01],
       [  74.  ,  220.  ,   24.81],
       [  68.  ,  180.  ,   28.79],
       [  72.  ,  185.  ,   33.77],
       [  75.  ,  200.  ,   33.85],
       [  71.  ,  210.  ,   27.36],
       [  70.  ,  220.  ,   26.01],
       [  72.  ,  185.  ,   29.95],
       [  73.  ,  231.  ,   28.12],
       [  72.  ,  210.  ,   32.87],
       [  75.  ,  195.  ,   31.2 ],
       [  74.  ,  200.  ,   34.14],
       [  70.  ,  205.  ,   36.11],
       [  76.  ,  200.  ,   26.31],
       [  71.  ,  190.  ,   27.5 ],
       [  82.  ,  250.  ,   27.77],
       [  72.  ,  185.  ,   40.88],
       [  73.  ,  180.  ,   25.75],
       [  74.  ,  170.  ,   31.41],
       [  71.  ,  180.  ,   30.84],
       [  75.  ,  208.  ,   30.57],
       [  77.  ,  235.  ,   39.79],
       [  72.  ,  215.  ,   39.38],
       [  74.  ,  244.  ,   29.42],
       [  72.  ,  220.  ,   26.19],
       [  73.  ,  185.  ,   23.74],
       [  78.  ,  230.  ,   26.03],
       [  77.  ,  190.  ,   28.59],
       [  73.  ,  200.  ,   26.77],
       [  73.  ,  180.  ,   27.21],
       [  73.  ,  190.  ,   24.87],
       [  73.  ,  196.  ,   30.26],
       [  73.  ,  180.  ,   22.34],
       [  76.  ,  230.  ,   26.2 ],
       [  75.  ,  224.  ,   28.45],
       [  70.  ,  160.  ,   27.63],
       [  73.  ,  178.  ,   25.93],
       [  72.  ,  205.  ,   28.94],
       [  73.  ,  185.  ,   26.8 ],
       [  75.  ,  210.  ,   22.42],
       [  74.  ,  180.  ,   27.26],
       [  73.  ,  190.  ,   28.38],
       [  73.  ,  200.  ,   25.23],
       [  76.  ,  257.  ,   28.16],
       [  73.  ,  190.  ,   28.48],
       [  75.  ,  220.  ,   26.78],
       [  70.  ,  165.  ,   25.24],
       [  77.  ,  205.  ,   27.45],
       [  72.  ,  200.  ,   29.05],
       [  77.  ,  208.  ,   29.08],
       [  74.  ,  185.  ,   25.84],
       [  75.  ,  215.  ,   25.4 ],
       [  75.  ,  170.  ,   26.54],
       [  75.  ,  235.  ,   22.73],
       [  75.  ,  210.  ,   28.53],
       [  72.  ,  170.  ,   25.37],
       [  74.  ,  180.  ,   25.35],
       [  71.  ,  170.  ,   26.43],
       [  76.  ,  190.  ,   25.43],
       [  71.  ,  150.  ,   29.23],
       [  75.  ,  230.  ,   30.22],
       [  76.  ,  203.  ,   32.3 ],
       [  83.  ,  260.  ,   28.42],
       [  75.  ,  246.  ,   25.24],
       [  74.  ,  186.  ,   29.13],
       [  76.  ,  210.  ,   24.63],
       [  72.  ,  198.  ,   24.95],
       [  72.  ,  210.  ,   28.06],
       [  75.  ,  215.  ,   25.86],
       [  75.  ,  180.  ,   27.32],
       [  72.  ,  200.  ,   25.91],
       [  77.  ,  245.  ,   26.63],
       [  73.  ,  200.  ,   25.95],
       [  72.  ,  192.  ,   29.17],
       [  70.  ,  192.  ,   29.19],
       [  74.  ,  200.  ,   28.44],
       [  72.  ,  192.  ,   26.36],
       [  74.  ,  205.  ,   28.29],
       [  72.  ,  190.  ,   29.45],
       [  71.  ,  186.  ,   25.34],
       [  70.  ,  170.  ,   26.86],
       [  71.  ,  197.  ,   26.36],
       [  76.  ,  219.  ,   27.39],
       [  74.  ,  200.  ,   25.84],
       [  76.  ,  220.  ,   25.08],
       [  74.  ,  207.  ,   23.87],
       [  74.  ,  225.  ,   24.68],
       [  74.  ,  207.  ,   24.64],
       [  75.  ,  212.  ,   29.19],
       [  75.  ,  225.  ,   28.84],
       [  71.  ,  170.  ,   25.33],
       [  71.  ,  190.  ,   24.45],
       [  74.  ,  210.  ,   28.32],
       [  77.  ,  230.  ,   32.34],
       [  71.  ,  210.  ,   34.97],
       [  74.  ,  200.  ,   32.04],
       [  75.  ,  238.  ,   23.49],
       [  77.  ,  234.  ,   26.09],
       [  76.  ,  222.  ,   26.41],
       [  74.  ,  200.  ,   26.55],
       [  76.  ,  190.  ,   24.62],
       [  72.  ,  170.  ,   28.49],
       [  71.  ,  220.  ,   32.61],
       [  72.  ,  223.  ,   28.06],
       [  75.  ,  210.  ,   28.08],
       [  73.  ,  215.  ,   37.34],
       [  68.  ,  196.  ,   35.25],
       [  72.  ,  175.  ,   24.77],
       [  69.  ,  175.  ,   39.85],
       [  73.  ,  189.  ,   35.49],
       [  73.  ,  205.  ,   31.84],
       [  75.  ,  210.  ,   26.67],
       [  70.  ,  180.  ,   34.75],
       [  70.  ,  180.  ,   28.91],
       [  74.  ,  197.  ,   32.73],
       [  75.  ,  220.  ,   35.72],
       [  74.  ,  228.  ,   42.6 ],
       [  74.  ,  190.  ,   26.22],
       [  73.  ,  204.  ,   21.85],
       [  74.  ,  165.  ,   24.28],
       [  75.  ,  216.  ,   22.41],
       [  77.  ,  220.  ,   32.56],
       [  73.  ,  208.  ,   32.74],
       [  74.  ,  210.  ,   26.39],
       [  76.  ,  215.  ,   28.8 ],
       [  74.  ,  195.  ,   28.2 ],
       [  75.  ,  200.  ,   26.52],
       [  73.  ,  215.  ,   34.52],
       [  76.  ,  229.  ,   34.32],
       [  78.  ,  240.  ,   26.98],
       [  75.  ,  207.  ,   28.86],
       [  73.  ,  205.  ,   24.96],
       [  77.  ,  208.  ,   25.3 ],
       [  74.  ,  185.  ,   27.06],
       [  72.  ,  190.  ,   25.44],
       [  74.  ,  170.  ,   25.53],
       [  72.  ,  208.  ,   34.87],
       [  71.  ,  225.  ,   24.63],
       [  73.  ,  190.  ,   27.99],
       [  75.  ,  225.  ,   27.12],
       [  73.  ,  185.  ,   31.14],
       [  67.  ,  180.  ,   30.21],
       [  67.  ,  165.  ,   32.11],
       [  76.  ,  240.  ,   31.91],
       [  74.  ,  220.  ,   34.44],
       [  73.  ,  212.  ,   36.68],
       [  70.  ,  163.  ,   37.66],
       [  75.  ,  215.  ,   30.98],
       [  70.  ,  175.  ,   27.07],
       [  72.  ,  205.  ,   29.11],
       [  77.  ,  210.  ,   25.82],
       [  79.  ,  205.  ,   25.5 ],
       [  78.  ,  208.  ,   29.57],
       [  74.  ,  215.  ,   25.37],
       [  75.  ,  180.  ,   33.99],
       [  75.  ,  200.  ,   29.86],
       [  78.  ,  230.  ,   31.84],
       [  76.  ,  211.  ,   38.31],
       [  75.  ,  230.  ,   34.48],
       [  69.  ,  190.  ,   36.88],
       [  75.  ,  220.  ,   32.34],
       [  72.  ,  180.  ,   31.58],
       [  75.  ,  205.  ,   28.89],
       [  73.  ,  190.  ,   25.08],
       [  74.  ,  180.  ,   25.73],
       [  75.  ,  205.  ,   25.19],
       [  75.  ,  190.  ,   31.01],
       [  73.  ,  195.  ,   27.92]])
