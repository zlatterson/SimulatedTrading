import React,{useState, useEffect} from 'react';
import { Row, Col, Container } from 'react-bootstrap';
import logo from '../assets/img/logo.svg'
import navIcon1 from '../assets/img/nav-icon1.svg';
import navIcon2 from '../assets/img/nav-icon2.svg';
import navIcon3 from '../assets/img/nav-icon3.svg';

const Skills = ({}) => {


    return (
        <section className = "skill" id="skills">
            <Container>
                <Row>
                    <Col>
                    <div className='skill-bx'>
                        <h2>
                            Skills
                        </h2>
                        <p>In this tutorial, we build a personal portfolio website using React and Animate CSS. Follow along and share what you build in the comments!</p>
                    </div>
                    </Col>
                </Row>
            </Container>
        </section>
      );
}

export default Skills;