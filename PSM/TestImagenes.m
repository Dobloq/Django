% -------------- Test de Laboratorio --------------
% Autor: Alberto J. Molina
%
% Ficheros a usar:
% Helicoptero.jpg
% TestExpansion.m
% imhist.m
% imRealceExpansion.m  <---- A COMPLETAR
%--------------------------------------------------

clear all;
close all;
clc


%Leemos el fichero de entrada y lo representamos
in=imread('helicopter.jpg');
figure();
imshow(in);


%Obtenemos el histograma y lo representamos
hisin = imhist(in);
figure();
stem (hisin);


%Ecualizamos la imagen y representamos su histograma
out = imRealceExpansion(in,5,140); %<- A COMPLETAR POR EL ALUMNO
figure();
imshow(out);

hisout = imhist(out);
[maxval, row] = max(hisout);
row
figure();
stem(hisout);








