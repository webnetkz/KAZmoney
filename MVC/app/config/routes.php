<?php
return [
// Создаем массив для названий маршрутов
 '' => [
  'controller' => 'main', // Controller
  'action' => 'index', // Action
 ],

 'contact' => [
  'controller' => 'main',
  'action' => 'contact',
 ],

 'account/login' => [
  'controller' => 'account',
  'action' => 'login',
 ],

 'account/register' => [
 'controller' => 'account',
 'action' => 'register',
 ],

 'news/show' => [
  'controller' => 'news',
  'action' => 'show',
 ],
];
