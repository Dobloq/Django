% Test
clear all
close all
clc

%---------------------------------------------
% NO REUTILIZAR LAS VARIABLES n y N
%---------------------------------------------

%---------------------------------------------------
% Parte 1
%
% Creamos la respuesta impulsiva, h, de un filtro paso baja con una
% frecuencia de corte normalizada a Nyquist de 0.4. Para ello
% se usará la función hideal.m. Utilizando N=101 coeficientes
% 
%  h = hideal(...);
%

	h=hideal(101,200,1000);	%A COMPLETAR POR EL ALUMNO


%Representamos valores y generamos variables globales
	 
	N=length(h);    %N -> longitud de datos
	n=0:N-1;	%n   -> [0,1,2,.... N-1]

	stem(n,h,'linewidth',2,'filled');	%Representamos datos
	grid on;
	xlabel('n');
	ylabel('h[h]');
	title('Parte 1');
	%Complete las cuestiones de la hoja del test


%---------------------------------------------------
% Parte 2
%
% Ahora hay que calcular la fft de la respuesta impulsiva
% y representar su módulo en un gráfico donde el eje de 
% abscisas contiene la frecuencia normalizada f en el
% intervalo de  [0,1]. Recuerde que f = k/N donde k=0...N-1.
%
%
  
	modfft = abs(fft(h)); %A COMPLETAR POR EL ALUMNO
	f = n/N;%A COMPLETAR POR EL ALUMNO
  
	
	figure();
	plot(f,modfft,'-o','linewidth',2);
	xlabel('f');
	ylabel('modfft');
	title('Parte 2');
	grid on;

%Dibuje el resultado en la hoja del test

%---------------------------------------------------
% Parte 3
%
% Multiplicaremos la respuesta impulsiva por una ventana
% de Hann.
%
	
	% Bucle for .. end en el que creamos la ventana
	% de Hann que es una función del tipo
	% v= 0.5-0.5cos(2 pi n /(N-1))
	%
	% hv = h * v;
	%---------------------------------------------
	n = 0:N-1;
  v=0.5-0.5*cos(2*pi*n/(N-1));
	hv=h(:).*v(:);

			%A COMPLETAR POR EL ALUMNO

	%Para mostrar por consola los coeficientes
	if length(hv)==N
	%Para mostrar por consola los coeficientes
		printf('\n------------------\n');
		printf(strcat('| hv[9] = ',num2str(hv(10),2),' |\n'));
		printf(strcat('| hv[29] = ',num2str(hv(30),2),'  |\n'));
		printf(strcat('| hv[30] = ',num2str(hv(31),2),' |\n'));
		printf(strcat('| hv[31] = ',num2str(hv(32),2),' |\n'));
		printf('------------------\n');
		%Representamos la secuencia 
		figure();
		stem(n,hv,'linewidth',2,'filled');	%Representamos datos
		grid on;
		xlabel('n');
		ylabel('hv[h]');
		title('Parte 3');
	endif
	%Complete las cuestiones de la hoja del test


%---------------------------------------------------
% Parte 4
%
% Representación de datos

	modfft = abs(fft(hv)); %A COMPLETAR POR EL ALUMNO
	f = n/N;%A COMPLETAR POR EL ALUMNO
	
	figure();
	plot(f,modfft,'-o','linewidth',2);
	xlabel('f');
	ylabel('modfft');
	title('Parte 4');
	grid on;

%Dibuje el resultado en la hoja del test y
%complete las cuestiones de la hoja del test


%---------------------------------------------------
% Parte 5
%
% Ahora hay que calcular la fft de la respuesta impulsiva
% de la secuencia hd[n] obtenida haciendo 2 *hv[n] * cos (2*pi*f0*n), 
% donde f0 = 0.25c/m

	%A COMPLETAR POR EL ALUMNO
  coseno = 2*cos(2*pi*0.25*n)
	hd = hv(:).*coseno(:);

	modfft = abs(fft(hd)); %A COMPLETAR POR EL ALUMNO
	f = n/N;%A COMPLETAR POR EL ALUMNO
		
	figure();
	plot(f,modfft,'-o','linewidth',1.5);
	xlabel('f');
	ylabel('modfft');
	title('Parte 5');
	grid on;


%Dibuje el resultado en la hoja del test

%-------------------------------------------------------------
%Parte 6
% Interpolación I=2 de la señal h[n]
%	
	I=2;
	
	
	%----------------------------------------------
	% Bucle for donde m varia desde 0 a I*N-1
	% si la parte entera entre m/I es 0, entonces
	%   hinter = h( m/I+1)
	% en caso contrario 
	%   hinter = 0
	%----------------------------------------------
  for m = 0:I*(N-1)
    m
    I
    if(mod(m,I) == 0)
      hinter(m+1) = h(m/I+1);
    else
      hinter(m+1) = 0;
    endif
  endfor
	
	
	modfft = abs(fft(hinter)); %A COMPLETAR POR EL ALUMNO
  n = 0:2*(N-1);
	f = n/N/2;%A COMPLETAR POR EL ALUMNO
		
	figure();
	plot(f,modfft,'-o','linewidth',1.5);
	xlabel('f');
	ylabel('modfft');
	title('Parte 6');
	grid on;


%Dibuje el resultado en la hoja del test
%Complete las cuestiones de la hoja del test
