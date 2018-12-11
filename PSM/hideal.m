%----------------------------------------------------
%  		LABORATORIO 3
%
%Autor: Alberto J. Molina
%Fecha: 07/13
%Versión:1
%Modificaciones a la versión anterior: Ninguna.
%Versión: 2
%Fecha: 24/18
%Autor: Manuel Merino Monge
%Modificaciones a la versión anterior: Se modifica
%	los comentarios para facilitar la compresión de
%	la tarea.

%Respuesta impulsiva ideal
%Pertenece al apartado


function y = hideal (L, Fc, Fs);

%------------------------------------------
%	Argumentos de entrada (<-)
%		L : Longitud del filtro	 
%		Fc: Frecuencia de corte
%		Fs: Frecuencia de muestreo
%	Argumentos de salida (->)
%		y: Coeficientes del filtro paso de baja
%------------------------------------------

	y= zeros(L,1);  % Respuesta del filtro
		

	%----------------------------------------------------
	%  Calculamos la frecuencia de corte normalizada
	%----------------------------------------------------

    fc = Fc/Fs;  % A COMPLETAR POR EL ALUMNO

	%----------------------------------------------------
	%  Determinamos los coeficientes del filtro
    %----------------------------------------------------
	%
	%	1.- Empleando la función sinc de octave. Mirar la documentación de sinc.
	%		El dominio de esta función va desde -Inf a +Inf. y se define como:
	%
	%			sinc( x ) = sen ( pi * x )/ ( pi * x )
	%
	%		siendo siendo una función par sinc( -x ) = sinc( x ).
	%
	%		a.- Generar el vector X de longitud L con todos los enteros que van desde 
	%			-(L-1)/2 hasta (L-1) / 2
	%		b.- Generar un vector w que sea igual al vector X multiplicado por 2 veces
	%			la frecuencia de corte normalizada.
	%	
	% Nota: si octave no tuviera la función sinc( x ), resolver este apartado empleando 
	% su fórmula matemática:
	%
	%		sin ( pi * x )/ ( pi * x )
	%
	% sabiendo que para x = 0 se tiene una indeterminación del tipo (0 / 0), y su valor 
	% es sinc( 0 ) = 1.
	%----------------------------------------------------
  

              % A COMPLETAR POR EL ALUMNO
 
	%----------------------------------------------------
	
	M=(L-1)/2;
	
	
	for(n=0:L-1)
    if(n==M)
      y(n+1) = 2*fc;
    else
      y(n+1)=sinc(2*fc*(n-M))*2*fc;
    endif
  endfor
	
endfunction


