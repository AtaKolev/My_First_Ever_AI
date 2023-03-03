action_probability = {"N" : 0.166,
                      "E" : 0.166,
                      "S" : 0.166,
                      "W" : 0.166,
                      "NE" : 0.083,
                      "NW" : 0.083,
                      "SE" : 0.083,
                      "SW" : 0.083}

special_case_probability = {"N" : 0.2,
                            "E" : 0.1143,
                            "S" : 0.1143,
                            "W" : 0.1143,
                            "NE" : 0.1143,
                            "NW" : 0.1143,
                            "SE" : 0.1143,
                            "SW" : 0.1143}

movements = {"N" : (1, 0),
             "E" : (0, 1),
             "W" : (0, -1),
             "S" : (-1, 0),
             "NE" : (1, 1),
             "NW" : (1, -1),
             "SE" : (-1, 1),
             "SW" : (-1, -1)}

gamma = 0.9
learning_tolerance = 1e-7