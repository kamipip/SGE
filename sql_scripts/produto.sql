-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 09-Fev-2023 às 14:45
-- Versão do servidor: 10.4.24-MariaDB
-- versão do PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `produto`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `informacoes_produto`
--

CREATE TABLE `informacoes_produto` (
  `nome` varchar(255) DEFAULT NULL,
  `valor` int(11) DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `destino` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `informacoes_produto`
--

INSERT INTO `informacoes_produto` (`nome`, `valor`, `quantidade`, `destino`) VALUES
('maça', 500, 300, NULL),
('asdasd', 12, 12, NULL),
('Metal', 1000, 25, NULL),
('sadasd', 123123, 20, NULL),
('Metal', 1000, 25, NULL),
('Metal', 1000, 25, NULL),
('nome', 0, 1231231, NULL),
('adadad', 21, 213123, 'adsad'),
('asdasd', 20, 123123, '123123'),
('Metal', 25, 1000, '123123123'),
('Metal', 25, 1000, '123123123'),
('Metal', 25, 1000, '123123123'),
('sdaqsd', 19, 123123, '123123'),
('123123', 19, 123213, '123123123'),
('asdasd', 19, 1221, 'asdad'),
('comfortably_numb', 19, 1231, 'pink_floyd'),
('benedict', 19, 21312, 'cumberbatch'),
('asdasd', 19, 123123, 'skilet'),
('sdasd', 18, 123123, 'sdasdsad'),
('sdadasd', 18, 123123, 'adasd'),
('adasd', 19, 23123, '123123123'),
('asdasda', 19, 12312312, 'asdadasdad'),
('asdasd', 19, 123123, '123123123'),
('asdasd', 19, 123123, 'adadasd'),
('asdasd', 19, 2147483647, 'homem_aranha'),
('please', 18, 123123, 'dont'),
('charada', 19, 123123123, '12123123'),
('nemo', 20, 12121, 'dolky'),
('carmem', 19, 1231231231, 'asdasda'),
('severus', 19, 12, 'snape'),
('carmem', 18, 12312, 'beatriz'),
('record', 18, 123123, 'globo'),
('buck', 19, 123123, 'buck'),
('bruno', 19, 213123, 'mars'),
('bruno', 19, 23123, 'mars'),
('bruno', 19, 123123, 'mars'),
('grande', 19, 23123112, 'bruno mars'),
('asdasd', 19, 1231212, '12123'),
('produto12', 19, 123123, 'produto13'),
('talking_to', 19, 212, 'moon'),
('bruno', 18, 1212, 'mars'),
('cello', 19, 123123, 'green'),
('comma', 20, 56, '12123'),
('forbes', 19, 12, '123123'),
('1212', 19, 121212, '1212'),
('jeff', 19, 12, 'bezos'),
('nygma', 19, 1212, 'lil wayne'),
('produto34', 19, 12, 'filial700'),
('sdadsad', 19, 123123, 'filail'),
('produto45', 19, 12, 'XXRWEMatriz'),
('asdasd', 19, 123123, '123123123'),
('asdas', 20, 123123, '123123123'),
('asdasd', 21, 1231223, '123123123'),
('2w123', 19, 1212, 'GHJMatriz'),
('Metal', 21, 1000, '123123123'),
('23123', 19, 1231, '123123123'),
('asdasd', 19, 12312, '123123123'),
('alice', 20, 145, 'dest23'),
('1212', 21, 123123, '123123123'),
('123123', 21, 123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('Chervolet', 20, 123123123, '123123123'),
('xiacara', 20, 1231, 'ZR456Filial'),
('asdasd', 20, 123123123, 'ZR456Filial'),
('daft punk', 21, 123123, 'ZR456Filial'),
('daft punk', 21, 123123, 'ZR456Filial'),
('jhkjhjk', 21, 7687687, 'ZR456Filial'),
('maça', 50, 1200, 'ZR456Filial'),
('goiaba', 67, 1200, 'ZR456Filial'),
('chocolate', 60, 1200, 'ZR456Filial');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
