import math

dataset = [18.562874251497007, 20.958083832335326, 18.562874251497007, 19.161676646706585, 22.75449101796407]

diff = 100 - dataset.map(&:floor).reduce(&:+)

rounded_percentages = dataset
  .sort_by { |x| x.floor - x}
  .map
  .with_index { |e, index| index < diff ? e.floor + 1 : e.floor }
