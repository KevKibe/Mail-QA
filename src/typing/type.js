import React, { Component } from 'react';

class TypeWriter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: '',
      wordIndex: 0,
      isDeleting: false,
    };

    this.typeSpeed = 80; // Adjust this value to control typing speed
  }

  componentDidMount() {
    this.startTyping();
  }

  startTyping = () => {
    const { words, wait } = this.props;
    const current = this.state.wordIndex % words.length;
    const fullTxt = words[current];

    if (this.state.isDeleting) {
      this.setState({
        text: fullTxt.substring(0, this.state.text.length - 1),
      });
    } else {
      this.setState({
        text: fullTxt.substring(0, this.state.text.length + 1),
      });
    }

    if (this.state.isDeleting) {
      this.typeSpeed /= 2.5;
    }

    if (!this.state.isDeleting && this.state.text === fullTxt) {
      this.typeSpeed = wait;
      this.setState({
        isDeleting: true,
      });
    } else if (this.state.isDeleting && this.state.text === '') {
      this.setState({
        isDeleting: false,
        wordIndex: this.state.wordIndex + 1,
      });
      this.typeSpeed = 50;
    }

    setTimeout(this.startTyping, this.typeSpeed);
  };

  render() {
    return (
      <span className="txt">{this.state.text}</span>
    );
  }
}

export default TypeWriter;
