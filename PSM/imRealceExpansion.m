%-------------------------------------------------------
% Realce por funciones de de correspondencia lineales
% in -> Imagen de entrada (matriz)
% out <- Imagen de salida
% ngmin -> ngris mínimo al que se le asocia un ng = 0 en la imagen de salida
% ngmax -> ngris máximo al que se la asocia un ng = 255 en la imagen de salida
%-------------------------------------------------------

function out = imRealceExpansion( in , ngmin, ngmax);

	[m, n  ] =size(in);
	
	in = double(in);
  out = in;
	%----------------------------------------------------------------------
	%Ahora creamos la imagen nueva aplicando la función de correspondencia
	%Para cada pixel de la imagen de salida, se le aplica el nivel de gris
	%de la imagen original transformado por la función de correspondencia 
	%----------------------------------------------------------------------

	for i=1:m
		for j=1:n
			% Si el nivel de gris de la imagen de entrada es menor 
			% que ngmin, el nivel de gris de la salida es 0.
			% Si el nivel de gris de la imagen de entrada es mayor
			% que ngmax, el nivel de gris de la salida es 255
			% Para otro caso, el nivel de gris debe estar comprendido
			% entre 0 y 255 siguiendo una curva de correspondencia lineal
			%
			%	Véase transparencia 18 del  tema8
			%

			%A COMPLETAR
			if(in(i,j)<ngmin)
        out(i,j) = 0;
      elseif(in(i,j)>ngmax)
        out(i,j) = 255;
      else
        out(i,j) = 255/(ngmax-ngmin)*(in(i,j)-ngmin);
      endif
		endfor
	endfor
	
	out = uint8(out);
endfunction



