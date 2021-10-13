  
  node = find_lowest_cost_node (costs) # Найти узел с наименьшей стоимостью среди необработанных
  while node is not None:  # Если обработаны все узлы, цикл while завершен
    cost = costs[node]
    for n in neighbors.keys(): # Перебрать всех соседей текущего узла, если к соседу можно быстрее добраться через текущий узел
      new_cost = cost + neighbors[n]
      if costs[n] > new_cost:
         costs[n] = new_cost # Обновляем стоимость этого узла
         parents[n] = node  # Этот узел становится новым родителем для соседа
    processed.append(node) # Этот узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для обработки и повторить цикл
