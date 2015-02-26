set term png
set output "position_vs_time.png"
set xlabel "time"
set ylabel "position"
plot "Spring_Position.txt"

set output "Energy.png"
set ylabel "Total energy"

plot "Spring_KE.txt" with lines title 'Kinetic Energy', "Spring_PE.txt" with line lt -1 lw 1 title 'Potential Energy', "Spring_TE.txt" with line lt -1 lc rgb "red" lw 2 title 'Total Energy'

set output "Two spring(2).png"
set ylabel "Position"
plot "TS_1.txt" with points pt 1 ps 0.5 title 'Particle 1', "TS_2.txt" with lines title "particle 2" 